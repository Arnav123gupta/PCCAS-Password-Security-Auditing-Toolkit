<!-- PCCAS | Professional GitHub README -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=28&duration=2600&pause=800&color=00E5FF&center=true&vCenter=true&width=900&lines=PCCAS+%2F%2F+PASSWORD+SECURITY;AUDIT+%E2%80%A2+ANALYZE+%E2%80%A2+IMPROVE;DEFENSIVE+SECURITY+TOOLKIT" alt="PCCAS animated title" />

<p><strong>Python-based password security auditing and policy assessment toolkit.</strong></p>
<p><em>Understand password hygiene. Validate security policies. Learn through safe, synthetic simulations.</em></p>

<a href="https://github.com/Arnav123gupta/PCCAS-Password-Security-Auditing-Toolkit">
  <img src="https://img.shields.io/badge/GitHub-PCCAS-181717?style=for-the-badge&logo=github" alt="GitHub repository" />
</a>
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
<img src="https://img.shields.io/badge/Domain-Defensive%20Cybersecurity-087E8B?style=for-the-badge&logo=shield&logoColor=white" alt="Defensive cybersecurity" />
<img src="https://img.shields.io/badge/Project-Educational-6D28D9?style=for-the-badge" alt="Educational project" />

<p>
  <a href="#-overview">Overview</a> ·
  <a href="#-capabilities">Capabilities</a> ·
  <a href="#-installation">Installation</a> ·
  <a href="#-execution">Execution</a> ·
  <a href="#-security-scope">Security scope</a>
</p>

</div>

---

##  Contents

- [Overview](#-overview)
- [Capabilities](#-capabilities)
- [Architecture](#-architecture)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Execution](#-execution)
- [Testing](#-testing)
- [Output](#-output)
- [Security scope](#-security-scope)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)

##  Overview

**PCCAS (Password Security Auditing Toolkit)** is a Python educational project focused on defensive password-security concepts. It brings together password-strength indicators, configurable policy checks, structural hash-format hints, and a local account-lockout policy simulation.

The toolkit is intended to make core password-security checks easier to understand and demonstrate in a controlled environment.

> [!IMPORTANT]
> **Defensive-use boundary:** PCCAS uses synthetic examples and local simulations. It does not crack passwords, collect credentials, access accounts, or send login attempts to real services. Never enter real or reused passwords into test tools.

##  Capabilities

| Component | Responsibility | Output |
|---|---|---|
| Password analyzer | Reviews length and character-class indicators; flags a small sample of common values | Rating and recommendations |
| Test-data generator | Creates repeatable synthetic password examples | Local JSON dataset |
| Hash-format analyzer | Checks hexadecimal structure and length for possible format matches | Candidate format hints |
| Lockout simulator | Demonstrates a configurable lockout threshold and duration locally | Simulation result |
| Policy checker | Validates samples against configured password requirements | Pass/fail checks |
| Report generator | Saves demonstration results | JSON and TXT reports |

##  Architecture

```text
                  +----------------------+
                  |       main.py        |
                  |   Demo entry point   |
                  +----------+-----------+
                             |
          +------------------+------------------+
          |                  |                  |
          v                  v                  v
 +----------------+  +----------------+  +----------------+
 | Password       |  | Policy         |  | Hash-format    |
 | analyzer       |  | checker        |  | analyzer       |
 +----------------+  +----------------+  +----------------+
          |                  |                  |
          +------------------+------------------+
                             |
                 +-----------v-----------+
                 | Lockout policy        |
                 | simulation             |
                 +-----------+-----------+
                             |
                 +-----------v-----------+
                 | Report generator      |
                 | JSON / TXT            |
                 +-----------------------+
```

### Repository structure

```text
PCCAS/
├── data/                  # Synthetic sample datasets
├── docs/                  # Project documentation
├── modules/
│   ├── __init__.py
│   ├── password_analyzer.py
│   ├── dictionary_generator.py
│   ├── hash_format_analyzer.py
│   ├── attack_simulator.py
│   ├── policy_checker.py
│   └── report_generator.py
├── reports/               # Locally generated reports
├── screenshots/           # Project screenshots
├── tests/                 # Automated tests
├── main.py                # Demo entry point
├── requirements.txt
└── README.md
```

##  Requirements

- Python 3.10+
- pip
- Git

##  Installation

**1. Clone the repository**

```bash
git clone https://github.com/Arnav123gupta/PCCAS-Password-Security-Auditing-Toolkit.git
cd PCCAS-Password-Security-Auditing-Toolkit
```

**2. Create and activate a virtual environment**

Linux / Kali Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**3. Install project dependencies**

```bash
python -m pip install -r requirements.txt
```

##  Execution

Start the demonstration:

```bash
python main.py
```

The demo runs against built-in synthetic sample data. It does not connect to external services.

##  Testing

Run the test suite from the project root:

```bash
python -m pytest -v
```

Tests should be run after changes to confirm expected module behavior. Do not interpret a passing local test suite as proof of production readiness or comprehensive security.

##  Output

The demonstration generates local reports in the `reports/` directory:

- `pccas_report.json` — structured output for programmatic review.
- `pccas_report.txt` — human-readable summary.

Generated reports may contain sample values. Review them before sharing and keep real credentials out of the project.

##  Security scope

PCCAS is deliberately limited to defensive, non-invasive functionality.

- **Password scoring is approximate.** Character-set entropy is a theoretical estimate and does not fully represent human password choices, reuse, or predictable patterns.
- **Common-password detection is limited.** The built-in sample is small and is not a comprehensive breach corpus.
- **Hash identification is uncertain.** Length and character-set checks can suggest candidates but cannot reliably identify an algorithm.
- **Simulation is local only.** The lockout module demonstrates policy behavior without authenticating against a service.
- **Protect sensitive information.** Use synthetic data only; do not store production credentials, password dumps, or secrets in this repository.

##  Quality and security checks

Run the following checks from the project root:

```bash
python -m pytest -v
coverage run --branch -m pytest
coverage report -m
bandit -r main.py modules -ll
pip-audit -r requirements.txt
```

The password score and entropy value are simplified educational indicators,
not a security guarantee. Hash-format results are structural hints only.
All test data and lockout behavior are synthetic and local.

##  Roadmap

- [ ] Improve password-pattern analysis and document scoring assumptions.
- [ ] Expand policy configuration and edge-case tests.
- [ ] Add HTML report generation.
- [ ] Add reproducible security checks and coverage reporting.
- [ ] Expand architecture documentation and screenshots.

##  Contributing

Contributions are welcome when they improve defensive security, code quality, documentation, accessibility, or test coverage. Please keep changes within the project's safe educational scope.

##  Disclaimer

This project is provided for educational and defensive security awareness. Assess only data and systems you own or are explicitly authorized to assess. PCCAS is not a substitute for a professional security audit.

---

<div align="center">

**PCCAS — Password Security Auditing Toolkit**

<sub>Python · Password hygiene · Policy validation · Defensive security</sub>

</div>
