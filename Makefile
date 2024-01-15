.PHONY: 2021 2023

DAY=--help
PART=
BENCHMARK=

2021-test:
	@echo "Running lua tests"
	busted -C=./2021/lua

2021:


2023-test:
	@echo "Running python tests"
	pytest

2023:
	python -m 2023.python.main $(DAY) $(PART) $(BENCHMARK)
