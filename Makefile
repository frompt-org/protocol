# Foreign Prompts — dev tasks
LINT := bin/fp-lint
PROMPTS := $(wildcard prompts/*.prompt.md) TEMPLATE.prompt.md

.PHONY: help lint test

help:
	@echo "make lint   -- validate every .prompt.md in prompts/ and the template"
	@echo "make test   -- conformance suite: linter, adversarial probes, scaffolder"

lint:
	@$(LINT) $(PROMPTS)

test:
	@bin/fp-selftest
