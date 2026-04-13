.PHONY: test build

test:
	python3 -m pytest tests/ -v

build:
	python3 src/bootstrap_raw_placeholders.py
	jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=python3 --inplace notebooks/01_build_dataset.ipynb
	jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=python3 --inplace notebooks/02_compare_layers.ipynb
