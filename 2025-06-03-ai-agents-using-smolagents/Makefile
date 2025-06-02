#!/usr/bin/make -f

VENV = .venv
UV = uv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python

PYTEST_WATCH_MODULES =
ARGS =


venv-clean:
	@if [ -d "$(VENV)" ]; then \
		rm -rf "$(VENV)"; \
	fi

venv-create:
	$(UV) venv

dev-install:
	$(UV) sync

dev-venv: venv-create dev-install
