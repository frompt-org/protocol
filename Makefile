# Foreign Prompts — dev tasks
LINT := bin/fp-lint
PROMPTS := $(wildcard prompts/*/*.prompt.md) TEMPLATE.prompt.md

.PHONY: help lint test claims conform

help:
	@echo "make lint   -- validate every .prompt.md in prompts/ and the template"
	@echo "make claims -- check the docs still describe the tool that exists"
	@echo "make test   -- full conformance suite (linter, scaffolder, docs, regressions)"
	@echo "make conform AGENT=codex -- does a real agent behave as the protocol says?"

lint:
	@$(LINT) $(PROMPTS)

claims:
	@bin/fp-claimcheck .

test:
	@bin/fp-selftest

conform:
	@bin/fp-conform --agent $(or $(AGENT),codex)
