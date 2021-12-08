# Get root dir and project dir
PROJECT_ROOT ?= $(PWD)

BLACK ?= \033[0;30m
RED ?= \033[0;31m
GREEN ?= \033[0;32m
YELLOW ?= \033[0;33m
BLUE ?= \033[0;34m
PURPLE ?= \033[0;35m
CYAN ?= \033[0;36m
GRAY ?= \033[0;37m
COFF ?= \033[0m

# Mark non-file targets as PHONY
.PHONY: all help setup build

all: help


help:
	@printf "$(CYAN)make setup$(COFF)     - Sets up the project in your local machine\n"
	@printf "$(CYAN)make beautify$(COFF)  - Fixes styling by running black & isort\n"


setup:
	@printf "$(CYAN)Installing pre-commit hooks$(COFF)\n"
	pre-commit install

	@printf "$(CYAN)====================================================================\n"
	@printf "SETUP SUCCEEDED\n"


beautify:
	@echo pre-commit run --all-files
	@pre-commit run --all-files && echo "Your code was already pretty :-)" || echo "Fixed it for you!"
