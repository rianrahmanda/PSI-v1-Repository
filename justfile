set shell := ["bash", "-cu"]

VENV := ".venv"
PY := VENV + "/bin/python"

# List available recipes
default:
    @just --list

# Create local venv and install dependencies (ruff needed for lint/format)
[group('setup')]
install:
    python -m venv {{VENV}}
    {{PY}} -m pip install --upgrade pip
    {{PY}} -m pip install -r requirements.txt
    {{PY}} -m pip install ruff

# Run the Streamlit development server
[group('dev')]
dev:
    {{PY}} -m streamlit run app.py

# Test operations (unit|tidy)
[group('test')]
test action="unit":
    #!/usr/bin/env bash
    set -euo pipefail
    case "{{action}}" in
      unit) {{PY}} -m pytest -v ;;
      tidy) find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
            rm -rf .pytest_cache .ruff_cache ;;
      *)    echo "Unknown action: {{action}}"; exit 1 ;;
    esac

# Format operations — fix rewrites, check is dry-run for CI (fix|check)
[group('format')]
format action="fix":
    #!/usr/bin/env bash
    set -euo pipefail
    case "{{action}}" in
      fix)   {{PY}} -m ruff format . ;;
      check) {{PY}} -m ruff format --check . ;;
      *)     echo "Unknown action: {{action}}"; exit 1 ;;
    esac

# Lint operations — check reports issues, fix auto-corrects (check|fix)
[group('format')]
lint action="check":
    #!/usr/bin/env bash
    set -euo pipefail
    case "{{action}}" in
      check) {{PY}} -m ruff check . ;;
      fix)   {{PY}} -m ruff check --fix . ;;
      *)     echo "Unknown action: {{action}}"; exit 1 ;;
    esac
