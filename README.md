<!-- Animated header -->
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=26&duration=2800&pause=900&color=00F7FF&center=true&vCenter=true&width=850&lines=PCCAS+%7C+Password+Security+Auditing;Defensive+Security+%7C+Python+Toolkit;Analyze+%E2%80%A2+Audit+%E2%80%A2+Improve" alt="Animated PCCAS heading" />

<p><strong>A defensive, Python-based toolkit for password-strength review, policy validation, hash-format hints, and local lockout-policy demonstrations.</strong></p>

<p>
  <a href="https://github.com/Arnav123gupta/PCCAS-Password-Security-Auditing-Toolkit"><img src="https://img.shields.io/badge/PROJECT-PCCAS-111827?style=for-the-badge&logo=github&logoColor=white" alt="PCCAS repository" /></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/Focus-Defensive%20Security-16A34A?style=for-the-badge&logo=shield&logoColor=white" alt="Defensive security" />
  <img src="https://img.shields.io/badge/Status-Educational%20Project-7C3AED?style=for-the-badge" alt="Educational project" />
</p>

<p>
  <a href="#features"><img src="https://img.shields.io/badge/Explore-Features-0891B2?style=for-the-badge" alt="Explore features" /></a>
  <a href="#installation"><img src="https://img.shields.io/badge/Get-Started-2563EB?style=for-the-badge" alt="Get started" /></a>
  <a href="#safety-and-limitations"><img src="https://img.shields.io/badge/Read-Safety%20Notes-D97706?style=for-the-badge" alt="Safety notes" /></a>
</p>

</div>

---

## About

**PCCAS (Password Security Auditing Toolkit)** is an educational Python project for reviewing password-strength indicators, checking password policies, identifying *possible* hash formats from structural clues, and demonstrating account lockout policies using synthetic data.

> [!IMPORTANT]
> PCCAS is designed for defensive learning and local security awareness. It does **not** crack passwords, access accounts, collect credentials, or test real services. Use synthetic examples only.

## Features

| Module | Purpose |
|---|---|
| Password analyzer | Reviews length and character classes, flags a small set of common examples, and gives improvement suggestions |
| Synthetic test-data generator | Creates repeatable sample cases for local demonstrations |
| Hash-format analyzer | Provides possible format hints based on hexadecimal length and structure |
| Lockout-policy simulator | Demonstrates a configurable lockout threshold and duration locally |
| Policy checker | Evaluates sample strings against configurable password requirements |
| Report generator | Exports demonstration results in JSON and plain text |

## Project layout

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
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Arnav123gupta/PCCAS-Password-Security-Auditing-Toolkit.git
cd PCCAS-Password-Security-Auditing-Toolkit
```

### 2. Create a virtual environment

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

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the local demonstration:

```bash
python main.py
```

Run the automated test suite:

```bash
python -m pytest -v
```

The demonstration uses synthetic sample values and writes JSON and text reports to the local `reports/` directory.

## Safety and limitations

- Do not enter real, reused, sensitive, or production credentials into development tools or sample datasets.
- Password scores and entropy values are estimates, not guarantees of real-world resistance.
- Character-set entropy is a theoretical estimate and does not fully model human password choices or predictable patterns.
- The built-in common-password sample is intentionally small; it is not a comprehensive compromised-password database.
- Hash-format results are structural hints only. Different algorithms can produce strings with the same length and format.
- The lockout simulator is a local policy demonstration; it does not send authentication attempts to any service.

## Roadmap

- Improve password-pattern analysis and clearly explain scoring assumptions.
- Expand configurable policy options and validation tests.
- Add HTML report generation.
- Increase test coverage and add automated security checks.
- Add architecture documentation and usage examples.

## Contributing

Contributions focused on defensive security, documentation, test quality, and usability are welcome. Do not contribute credential theft, password cracking, or unauthorized-access functionality.

## Disclaimer

This project is provided for educational and defensive security purposes. Use it only with synthetic data or systems and information you are authorized to assess. The project is not a substitute for a professional security assessment.

---

<div align="center">

**PCCAS — Password Security Auditing Toolkit**

<sub>Built with Python · Focused on defensive security</sub>

</div>
