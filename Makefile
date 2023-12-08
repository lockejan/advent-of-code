.PHONY: 2021 2023

2021:
	@echo "Running lua tests"
	cd ./2021/lua/; \
		lua tests.lua

2023:
	@echo "Running python tests"
	pytest