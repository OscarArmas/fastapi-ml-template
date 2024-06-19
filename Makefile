#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`
VENV_PATH="$HOME/cascarone_ml"

# Python Interpreter
PYTHON_INTERPRETER = python3

#################################################################################
#                                COMMANDS                                       #
#################################################################################

#-----------------------#
# Project Setup         #
#-----------------------#

install:
	tools/create_env.sh
	source ${VENV_PATH}/bin/activate

#-----------------------#
# Code Style            #
#-----------------------#

codestyle:
	$(PYTHON_INTERPRETER) -m pyupgrade --exit-zero-even-if-changed --py39-plus **/*.py
	$(PYTHON_INTERPRETER) -m isort --settings-path pyproject.toml ./
	$(PYTHON_INTERPRETER) -m black --config pyproject.toml --exclude examples ./

#-----------------------#
# CI Pipeline           #
#-----------------------#

check-codestyle:
	$(PYTHON_INTERPRETER) -m isort --diff --check-only --settings-path pyproject.toml ./
	$(PYTHON_INTERPRETER) -m black --diff --check --config pyproject.toml ./

lint: test check-codestyle

test:
	$(PYTHON_INTERPRETER) -m pytest -v -c pyproject.toml tests/