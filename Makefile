# Foreign Prompts — dev tasks
LINT := bin/fp-lint
PROMPTS := $(wildcard prompts/*.prompt.md) TEMPLATE.prompt.md

.PHONY: help lint test

help:
	@echo "make lint   -- validate every .prompt.md in prompts/ and the template"
	@echo "make test   -- lint, plus assert the hostile fixture is rejected"

lint:
	@$(LINT) $(PROMPTS)

test: lint
	@if $(LINT) -q examples/hostile-sample.prompt.md.txt >/dev/null 2>&1; then \
		echo "FAIL: hostile fixture passed the linter"; exit 1; \
	else \
		echo "OK: hostile fixture rejected"; \
	fi
	@bin/fp-new selftest-prompt -c selftest-phrase --author ci | $(LINT) -q - && echo "OK: fp-new output is lint-clean"
	@echo "all good"
