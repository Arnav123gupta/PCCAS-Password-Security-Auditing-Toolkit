# PCCAS — Password Security Auditing Toolkit

PCCAS is a Python-based educational toolkit for reviewing password-strength indicators, checking password policies, identifying possible hash formats from their structure, and demonstrating account lockout policies with synthetic data.

> **Safety note:** PCCAS is designed for defensive learning and local security awareness. It does not attempt to crack passwords, access accounts, collect credentials, or test real services. Use synthetic examples only.

## Features

- **Password analysis** — checks length, character classes, a small built-in common-password sample, and provides recommendations.
- **Synthetic test-data generation** — creates sample password cases for repeatable local demonstrations.
- **Hash-format hints** — suggests possible hash families based on hexadecimal character and length patterns. These are hints, not definitive identification.
- **Lockout-policy simulation** — demonstrates a configurable lockout threshold and duration without sending login attempts to any service.
- **Password-policy checks** — evaluates samples against configurable length and character-class requirements.
- **Reports** — exports demonstration results as JSON and plain text.

## Project structure

```text
PCCAS/
├── data/                 # Synthetic sample data
├── docs/                 # Project documentation
├── modules/
│   ├── password_analyzer.py
│   ├── dictionary_generator.py
│   ├── hash_format_analyzer.py
│   ├── attack_simulator.py
│   ├── policy_checker.py
│   └── report_generator.py
├── reports/              # Generated local reports
├── screenshots/          # Project screenshots
├── tests/                # Automated tests
├── main.py               # Demo entry point
└── requirements.txt
```

## Requirements

- Python 3.10 or newer
- pip

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Arnav123gupta/PCCAS-Password-Security-Auditing-Toolkit.git
cd PCCAS-Password-Security-Auditing-Toolkit
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the demonstration

```bash
python main.py
```

The demo uses hard-coded synthetic sample data and writes JSON and text reports to the local `reports/` directory.

## Run tests

```bash
python -m pytest -v
```

## Important limitations

- Password-strength scores and entropy values are estimates, not guarantees of real-world resistance.
- Character-set entropy is a theoretical estimate and does not fully model human password choices or predictable patterns.
- The common-password sample is intentionally small and is not a comprehensive compromised-password database.
- Hash-format analysis is based on structural clues. Different algorithms can produce strings with the same format and length.
- The lockout simulator is a local policy demonstration only; it does not perform authentication attempts.
- Do not enter real, reused, sensitive, or production credentials into development tools or sample datasets.

## Roadmap

- Improve password-pattern analysis and explain scoring assumptions.
- Add richer policy configuration and validation tests.
- Add HTML report output.
- Expand test coverage and automated security checks.
- Improve documentation with examples and architecture notes.

## Contributing

Issues and pull requests for defensive improvements, documentation, test quality, and usability are welcome. Please do not contribute credential theft, password-cracking, or unauthorized-access functionality.

## Disclaimer

This project is provided for educational and defensive security purposes. The author is not responsible for misuse. Test only with data and systems you own or are explicitly authorized to assess.
