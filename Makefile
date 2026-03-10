SYSTEM_PYTHON_BINARY := python3
VIRTUAL_ENV := .venv
VIRTUAL_BIN := $(VIRTUAL_ENV)/bin
VIRTUAL_PYTHON_BINARY := $(VIRTUAL_BIN)/python3
PROJECT_NAME := coloradomesh
TEST_DIR := tests

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## build - Builds the project in preparation for release
build:
	$(VIRTUAL_PYTHON_BINARY) -m pip install build wheel
	rm -rf dist build *.egg-info
	$(VIRTUAL_PYTHON_BINARY) -m build --wheel --no-isolation --outdir dist/ .

## build-test - Builds the project for testing the build process
build-test:
	make temp-version
	make build

## coverage - Test the project and generate an HTML coverage report
coverage:
	$(VIRTUAL_BIN)/pytest --cov=$(PROJECT_NAME) --cov-branch --cov-report=html --cov-report=term-missing

## clean - Remove the virtual environment and clear out .pyc files
clean:
	rm -rf $(VIRTUAL_ENV)
	find . -name '*.pyc' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

## black - Runs the Black Python formatter against the project
black:
	$(VIRTUAL_BIN)/black $(PROJECT_NAME)/ $(TEST_DIR)/

## black-check - Checks if the project is formatted correctly against the Black rules
black-check:
	$(VIRTUAL_BIN)/black $(PROJECT_NAME)/ $(TEST_DIR)/ --check

## format - Runs all formatting tools against the project
format: black isort lint mypy

## format-check - Checks if the project is formatted correctly against all formatting rules
format-check: black-check isort-check lint mypy

## install - Install the project locally
install:
	$(SYSTEM_PYTHON_BINARY) -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_BIN)/pip install -e ."[dev]"

## install-pypy - Install the project locally using PyPy
install-pypy:
	$(SYSTEM_PYTHON_BINARY) -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_BIN)/pip install -e ."[pypy_dev]"

## install-pyenv - Install pyenv
install-pyenv:
	curl https://pyenv.run | bash

## change-python - Change the python version used by pyenv
# params:
# py - The python version to use
change-python:
	pyenv local $(py)

## isort - Sorts imports throughout the project
isort:
	$(VIRTUAL_BIN)/isort $(PROJECT_NAME)/ $(TEST_DIR)/

## isort-check - Checks that imports throughout the project are sorted correctly
isort-check:
	$(VIRTUAL_BIN)/isort $(PROJECT_NAME)/ $(TEST_DIR)/ --check-only

## lint - Lint the project
lint:
	$(VIRTUAL_BIN)/flake8 $(PROJECT_NAME)/ $(TEST_DIR)/

## mypy - Run mypy type checking on the project
mypy:
	$(VIRTUAL_BIN)/mypy $(PROJECT_NAME)/ $(TEST_DIR)/

## publish - Publish the project to PyPI
publish:
	twine upload dist/*

## temp-version - Set a temporary version for testing the build process
temp-version:
	make set-version version=0.0.1

## temp-version-revert - Revert the temporary version change
temp-version-revert:
	make set-version version=VERSIONADDEDBYGITHUB
	# Replace 0.0.1 with VERSIONADDEDBYGITHUB
	gsed -i 's/0.0.1/VERSIONADDEDBYGITHUB/g' pyproject.toml
	gsed -i 's/0.0.1/VERSIONADDEDBYGITHUB/g' $(PROJECT_NAME)/_version.py

## test - Test the project
test:
	$(VIRTUAL_BIN)/pytest --exitfirst --verbose --failed-first

## set-version - Set the version
# params:
# version - The version to set for the project
set-version:
	# Replace VERSIONADDEDBYGITHUB with version
	gsed -i 's/VERSIONADDEDBYGITHUB/$(version)/g' pyproject.toml
	gsed -i 's/VERSIONADDEDBYGITHUB/$(version)/g' $(PROJECT_NAME)/_version.py

.PHONY: help build coverage clean black black-check format format-check install install-pypy install-pyenv change-python isort isort-check lint mypy test
