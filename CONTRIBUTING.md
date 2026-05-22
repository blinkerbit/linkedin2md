# Contributing to linkedin2md

Thank you for your interest in contributing to linkedin2md! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/juanmanueldaza/linkedin2md.git
   cd linkedin2md
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

## Code Style

This project uses:
- **Ruff** for linting and formatting
- **Pyright** for type checking
- Line length: 88 characters
- Target: Python 3.13+

Run checks before submitting:
```bash
ruff check .
ruff format .
pyright
pytest
```

## Architecture

The project follows SOLID principles:

- **Single Responsibility**: Each parser/formatter handles one section
- **Open/Closed**: Add new parsers via `@register_parser` decorator
- **Liskov Substitution**: All parsers implement `SectionParser` protocol
- **Interface Segregation**: Focused protocols for each component
- **Dependency Inversion**: Converter depends on protocols, not implementations

### Adding a New Parser

1. Create a file in `src/linkedin2md/parsers/`
2. Implement the `SectionParser` protocol
3. Use `@register_parser` decorator
4. Create matching formatter in `src/linkedin2md/formatters/`

Example:
```python
from linkedin2md.parsers.base import BaseParser
from linkedin2md.registry import register_parser

@register_parser
class MyNewParser(BaseParser):
    section_key = "my_section"
    csv_files = ["MyData.csv"]
    
    def parse(self, data: dict) -> list:
        # Parse logic here
        return []
```

## Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Write tests** for new functionality
3. **Update documentation** if needed
4. **Ensure all checks pass** (ruff, pyright, pytest)
5. **Submit a PR** with a clear description

### AI-Assisted & Agentic Contributions (Optional)

This repository is equipped with **opencode** configurations and the **NERV** orchestration framework. You can use your own AI tools or NERV directly inside this repository to assist in coding and auditing:

*   **Initialize NERV environment**: Make sure you have `opencode` and `uv` installed, then run your local agent commands.
*   **Run Spec-Driven Development**: Initiate complex features or bug fixes via `/sdd-new <change_description>` to coordinate explorers, designers, planners, and code executors automatically.
*   **Adversarial Code Audit**: Run `/judgment-day` within the opencode terminal to trigger a dual-model adversarial code review. It will check compliance against our strict standards listed in `AGENTS.md` and export a clean synthetic audit table.

### PR Checklist

- [ ] Code follows the project style and `AGENTS.md` guidelines
- [ ] Tests added/updated (verify via `PYTHONPATH=src uv run pytest`)
- [ ] Documentation updated (if applicable)
- [ ] All CI/CD and lint checks pass

## Reporting Bugs

When reporting bugs, please include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Sample data (if possible, anonymized)

## Feature Requests

Feature requests are welcome! Please:
- Check existing issues first
- Describe the use case
- Explain why it would benefit others

## Questions?

Feel free to open an issue for questions or discussions.
