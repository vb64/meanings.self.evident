.PHONY: all setup
# make tests >debug.log 2>&1
ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
else
PYTHON = ./venv/bin/python
endif

PIP = $(PYTHON) -m pip install

all:
	$(PYTHON) to_docx.py

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip

setup_python:
	$(PYTHON_BIN) -m venv ./venv
