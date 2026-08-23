# Skill Injection — dev tasks
LINT := bin/claw-lint
SKILLS := $(wildcard skills/*.claw.md) TEMPLATE.claw.md

.PHONY: help lint test

help:
	@echo "make lint   -- validate every .claw.md in skills/ and the template"
	@echo "make test   -- lint, plus assert the hostile fixture is rejected"

lint:
	@$(LINT) $(SKILLS)

test: lint
	@if $(LINT) -q examples/hostile-sample.claw.md.txt >/dev/null 2>&1; then \
		echo "FAIL: hostile fixture passed the linter"; exit 1; \
	else \
		echo "OK: hostile fixture rejected"; \
	fi
	@bin/claw-new selftest-skill --author ci | $(LINT) -q - && echo "OK: claw-new output is lint-clean"
	@echo "all good"
