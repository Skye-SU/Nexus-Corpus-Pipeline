from __future__ import annotations

from collections import defaultdict

LINK_FIELDS = [
    "link_id",
    "from_doc_id",
    "to_doc_id",
    "relation_type",
    "evidence",
    "confidence",
    "notes",
]

LINK_OVERRIDES = {
    "us-01__news__news_1": {
        "to_doc_id": "us-01__official__anchor",
        "relation_type": "reports_on",
        "evidence": "official_news_release_on_same_guidance",
        "confidence": "0.95",
        "notes": "Official NewsNet release tied directly to the same registration guidance initiative.",
    },
    "us-01__news__news_2": {
        "to_doc_id": "us-01__official__anchor",
        "relation_type": "reports_on",
        "evidence": "workflow_explainer_on_same_guidance",
        "confidence": "0.90",
        "notes": "Official explainer for the same guidance and registration workflow.",
    },
    "us-03__news__news_1": {
        "to_doc_id": "us-03__official__anchor",
        "relation_type": "reports_on",
        "evidence": "official_news_release_on_same_report",
        "confidence": "0.98",
        "notes": "Official NewsNet release announcing the same Part 2 report.",
    },
    "us-03__news__news_2": {
        "to_doc_id": "us-03__official__anchor",
        "relation_type": "reports_on",
        "evidence": "general_news_on_same_report",
        "confidence": "0.85",
        "notes": "General news coverage summarizing the same Copyright Office report.",
    },
    "us-03__news__news_3": {
        "to_doc_id": "us-03__official__anchor",
        "relation_type": "reports_on",
        "evidence": "tech_policy_coverage_of_same_report",
        "confidence": "0.85",
        "notes": "Tech-policy coverage restating the same report's negative boundary case.",
    },
    "cn-04__news__news_1": {
        "to_doc_id": "cn-04__official__anchor",
        "relation_type": "reports_on",
        "evidence": "state_media_explainer_on_same_measures",
        "confidence": "0.92",
        "notes": "State-media explanation directly summarizing the same labeling measures.",
    },
    "cn-04__news__news_2": {
        "to_doc_id": "cn-04__official__anchor",
        "relation_type": "reports_on",
        "evidence": "state_media_rollout_notice_on_same_measures",
        "confidence": "0.90",
        "notes": "State-media rollout notice tied directly to the same four-agency labeling measures.",
    },
}


def build_link_scaffold(documents: list[dict[str, str]]) -> list[dict[str, str]]:
    by_packet: dict[str, list[dict[str, str]]] = defaultdict(list)
    for document in documents:
        by_packet[document["packet_id"]].append(document)

    links = []
    for packet_id, packet_docs in by_packet.items():
        anchors = [doc for doc in packet_docs if doc["layer"] == "official"]
        if not anchors:
            continue
        anchor = anchors[0]
        news_docs = [doc for doc in packet_docs if doc["layer"] == "news"]
        social_docs = [doc for doc in packet_docs if doc["layer"] == "social"]

        for index, news_doc in enumerate(news_docs, start=1):
            link = {
                "link_id": f"{packet_id.lower()}__news__{index}",
                "from_doc_id": news_doc["doc_id"],
                "to_doc_id": anchor["doc_id"],
                "relation_type": "reports_on",
                "evidence": "packet_membership",
                "confidence": "0.30",
                "notes": "Link inferred from shared packet membership.",
            }
            link.update(LINK_OVERRIDES.get(news_doc["doc_id"], {}))
            links.append(link)

        for index, social_doc in enumerate(social_docs, start=1):
            links.append(
                {
                    "link_id": f"{packet_id.lower()}__social__{index}",
                    "from_doc_id": social_doc["doc_id"],
                    "to_doc_id": anchor["doc_id"],
                    "relation_type": "reposts_or_discusses",
                    "evidence": "packet_membership",
                    "confidence": "0.20",
                    "notes": "Packet-level link; individual verification pending.",
                }
            )

    return links
