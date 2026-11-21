<!-- PCCAS | Password Security Auditing Toolkit -->

<div align="center">

# PCCAS
### Password Security Auditing Toolkit

**A Python-based educational toolkit for understanding password hygiene and defensive password-policy checks.**

Analyze · Validate · Simulate · Report

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/Tests-35%20passed-2E8B57?style=for-the-badge&logo=pytest&logoColor=white" alt="35 tests passed" />
  <img src="https://img.shields.io/badge/Coverage-94%25-087E8B?style=for-the-badge" alt="94 percent coverage" />
  <img src="https://img.shields.io/badge/Use-Defensive%20%26%20Educational-6D28D9?style=for-the-badge" alt="Defensive and educational" />
</p>

[Overview](#overview) · [Features](#features) · [Setup](#setup) · [Usage](#usage) · [Testing](#testing) · [Security scope](#security-scope)

</div>

---

## Overview

**PCCAS (Password Security Auditing Toolkit)** is a Python project that brings together several foundational password-security concepts in one local, educational workflow. It provides approximate password-strength indicators, configurable policy validation, structural hash-format hints, synthetic sample-data generation, a local lockout-policy simulation, and report generation.

The project is designed for learning, demonstration, and defensive security awareness. It is not a password-cracking tool and does not interact with real login services.

> [!IMPORTANT]
> **Use synthetic test data only.** Do not enter real, reused, or production passwords. PCCAS does not collect credentials, crack hashes, access accounts, or send authentication attempts to external services.

## Features

| Module | What it does |
|---|---|
| Password analyzer | Reviews password length and character-class indicators, and provides improvement suggestions |
| Synthetic data generator | Creates a small set of sample records for repeatable local demonstrations |
| Hash-format analyzer | Examines hexadecimal structure and length to return possible format hints |
| Lockout simulator | Demonstrates configurable attempt thresholds and lockout duration locally |
| Policy checker | Checks sample passwords against configured policy requirements |
| Report generator | Writes demonstration results in JSON and plain-text formats |

### How the workflow fits together

```text
                     main.py
                (demo entry point)
                       |
          +------------+-------------+
          |            |             |
          v            v             v
   Password       Policy        Hash-format
   analyzer       checker        analyzer
          |            |             |
          +------------+-------------+
                       |
                       v
              Local lockout-policy
                  simulation
                       |
                       v
                Report generator
                  JSON / TXT
```

### Project structure

```text
PCCAS/
├── data/
│   ├── test_cases.json
│   └── hash_samples.json
├── modules/
│   ├── __init__.py
│   ├── attack_simulator.py
│   ├── dictionary_generator.py
│   ├── hash_format_analyzer.py
│   ├── password_analyzer.py
│   ├── policy_checker.py
│   └── report_generator.py
├── tests/
│   ├── test_attack_simulator.py
│   ├── test_dictionary_generator.py
│   ├── test_hash_format_analyzer.py
│   ├── test_main.py
│   ├── test_password_analyzer.py
│   ├── test_policy_checker.py
│   └── test_report_generator.py
├── main.py
├── requirements.txt
└── README.md
```

Generated reports are written to the local `reports/` directory. That directory is intentionally excluded from version control so generated output is not accidentally committed.

## Requirements

- Python 3.10 or newer
- pip
- Git

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Arnav123gupta/PCCAS-Password-Security-Auditing-Toolkit.git
cd PCCAS-Password-Security-Auditing-Toolkit
```

### 2. Create and activate a virtual environment

**Linux / Kali Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install project dependencies

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the local demonstration from the repository root:

```bash
python main.py
```

The demo uses local synthetic examples. It does not connect to websites, external APIs, or authentication services.

### Generated reports

The report generator creates:

- `reports/pccas_report.json` — structured report data.
- `reports/pccas_report.txt` — a readable text summary.

Inspect generated reports before sharing them. Keep real credentials and secrets out of report files and the repository.

## Testing

Run the automated test suite:

```bash
python -m pytest -v
```

### Latest verified project checks

At commit `60badce`, the project checks reported:

| Check | Result |
|---|---:|
| Automated tests | 35 passed |
| Branch-aware test coverage | 94% |
| Bandit scan (`-ll`) | No issues identified |
| pip-audit | No known vulnerabilities found |
| Python compilation | Passed |
| Synthetic JSON validation | Passed |

These are results from the recorded local audit, not a guarantee that every future revision or environment will produce the same results.

### Run the additional audit tools

The additional tools below are used for project auditing and are not part of the runtime requirements file. Install them separately when you want to reproduce the full audit:

```bash
python -m pip install coverage bandit pip-audit
coverage run --branch -m pytest
coverage report -m
bandit -r main.py modules -ll
pip-audit -r requirements.txt
python -m compileall -q main.py modules tests
python -m json.tool data/test_cases.json
python -m json.tool data/hash_samples.json
```

## Security scope and limitations

PCCAS is intentionally limited to defensive, non-invasive, local functionality.

- **Strength score is approximate:** the analyzer uses simplified indicators. Its score is not a guarantee of password strength and does not fully model human choice, reuse, or predictable patterns.
- **Common-password sample is limited:** the built-in examples are educational test data, not a comprehensive or current breach corpus.
- **Hash-format hints are inconclusive:** matching a length and character set cannot reliably identify a hash algorithm. Different formats can share the same structure.
- **Lockout behavior is simulated:** the module demonstrates a policy locally; it does not attempt authentication against a real account or service.
- **Synthetic data only:** do not add real passwords, password dumps, API keys, tokens, or other secrets to the repository.

PCCAS is an educational project, not a substitute for a professional security assessment or an enterprise password-management system.

## Roadmap

- [ ] Improve password-pattern analysis and document scoring assumptions.
- [ ] Expand policy configuration and edge-case coverage.
- [ ] Add HTML report generation.
- [ ] Add a reproducible CI workflow for tests and security checks.
- [ ] Add reviewed screenshots and expanded usage documentation.

## Contributing

Contributions that improve defensive security education, code quality, documentation, accessibility, or test coverage are welcome. Keep proposed changes within the project's safe, local, educational scope.

## Disclaimer

This project is provided for educational and defensive security awareness. Only assess data and systems you own or are explicitly authorized to assess. The maintainers make no guarantee that the toolkit is suitable for production security decisions.

---

<div align="center">

**PCCAS — Password Security Auditing Toolkit**

*Python · Password hygiene · Policy validation · Defensive security*

</div>
