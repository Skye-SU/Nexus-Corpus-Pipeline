# Project Overview

Last updated: 2026-04-13

## Purpose

This repository provides a notebook-first research text infrastructure for cross-jurisdictional analysis of generative AI copyright law. It organizes primary legal sources, news coverage, and social discourse into reusable, linked data packets covering:

- Generative AI copyright and authorship doctrine
- Originality requirements for AI-generated and AI-assisted works
- AI-related copyright regulation and public discourse

## Jurisdictional Coverage

The current corpus spans two jurisdictions:

- **United States**: Copyright Office registration guidance, the Thaler v. Perlmutter human-authorship line, and the Part 2 copyrightability report
- **China**: The Beijing Internet Court AI-generated image copyright case and the synthetic content labeling measures

## Data Architecture

Each source packet is organized across three layers:

| Layer | Content |
|-------|---------|
| **Official** | Primary legal, regulatory, or policy texts |
| **News** | Journalistic and professional coverage |
| **Social** | Public discourse and commentary |

## Current Build State

- **Packets**: US-01, US-02, US-03, CN-02, CN-04
- **Documents**: 29
- **Cross-layer links**: 24
- **Text extraction coverage**: to be verified after pipeline re-execution

## Analytical Observations

### 1. Legal reasoning compresses as it moves from official to public layers

In the U.S. authorship packets, official texts emphasize human contribution, expressive control, and copyrightability criteria. News and social layers reduce these to shorter public-facing questions: whether AI-generated works can be protected and whether the human operator qualifies as the author.

### 2. The China AI image case demonstrates a reasoning-to-outcome compression pattern

In the CN-02 packet, the court's analysis addresses intellectual input, selection, adjustment, and personalized expression at length. Downstream coverage compresses the reasoning into an outcome summary: the image was copyrightable, the user was recognized as the author, and infringement was established.

### 3. The labeling packet illustrates a distinct regulatory propagation pattern

The CN-04 packet addresses content labeling rather than authorship. Its language is operational and platform-facing, centered on metadata tagging, disclosure obligations, and dissemination rules. This provides a useful comparison case showing how a governance rule propagates through official notice, media explanation, and social redistribution without engaging the core originality question.

## Applications

The packet structure supports:

- Data collection and cleaning demonstrations
- Cross-layer text comparison and similarity analysis
- Semantic analysis of how legal reasoning transforms across discourse layers
- Reusable notebook examples from a consistent, documented source base

## Scope Limitations

This infrastructure does not include:

- Frontend or interactive application components
- Chatbot or conversational AI features
- Comprehensive AI governance coverage beyond copyright

The value lies in the packet structure, source provenance, and reproducible data pipeline.

## Recommended Review Order

1. Read this overview
2. Open `notebooks/02_compare_layers.ipynb`
3. Inspect the repository structure for implementation details as needed
