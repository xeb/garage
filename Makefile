.PHONY: help

help:
	@echo "Garage Make Commands"
	@echo "---------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## Sets up the project from a fresh clone
	pip install -r requirements.txt
	pip install -e .
