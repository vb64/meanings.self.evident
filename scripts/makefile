.PHONY: all setup
# make tests >debug.log 2>&1
ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
else
PYTHON = ./venv/bin/python
endif

PIP = $(PYTHON) -m pip install

all:

md:
	$(PYTHON) make_md.py
docx:
	$(PYTHON) to_docx.py

srt:
	$(PYTHON) make_srt.py

single:
	$(PYTHON) make_srt.py single

txt:
	$(PYTHON) make_txt.py

trans:
	$(PYTHON) make_transcript.py

pdf:
	$(PYTHON) make_pdf.py

pdf1:
	$(PYTHON) make_pdf.py single

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv
