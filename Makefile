# Remote Skills — dev tasks
LINT := bin/skill-lint
SKILLS := $(wildcard skills/*.skill.md) TEMPLATE.skill.md

.PHONY: help lint test

help:
	@echo "make lint   -- validate every .skill.md in skills/ and the template"
	@echo "make test   -- lint, plus assert the hostile fixture is rejected"

lint:
	@$(LINT) $(SKILLS)

test: lint
	@if $(LINT) -q examples/hostile-sample.skill.md.txt >/dev/null 2>&1; then \
		echo "FAIL: hostile fixture passed the linter"; exit 1; \
	else \
		echo "OK: hostile fixture rejected"; \
	fi
	@bin/skill-new selftest-skill -k selftest --author ci | $(LINT) -q - && echo "OK: skill-new output is lint-clean"
	@echo "all good"
