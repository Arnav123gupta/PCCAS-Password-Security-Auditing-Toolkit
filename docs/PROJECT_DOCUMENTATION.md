# Password Cracking & Credential Attack Suite

## Project purpose
An educational toolkit for password policy testing and credential-security assessment using synthetic examples and local simulations.

## Modules
1. Dictionary test-data generator: creates labeled synthetic security test cases, not operational guessing lists.
2. Hash-format analyzer: provides structural hints for sample strings; it does not verify or crack hashes.
3. Linux Shadow / Windows SAM learning demo: displays synthetic record-format examples; it does not access system credential stores.
4. Brute-force resistance estimator: calculates a hypothetical search-space estimate without generating guesses or attempting authentication.
5. Password strength analyzer: estimates characteristics and provides recommendations.
6. Password policy checker: evaluates configurable local policy requirements.
7. Mock credential-risk assessment: evaluates synthetic labels for password reuse, common-password risk and MFA coverage.
8. Report generator: creates JSON and TXT audit reports.

## Run
```bash
python main.py
```

## Test
```bash
python -m pytest -v
```

## Deliverables
- Python source modules and automated tests
- Synthetic sample datasets
- JSON and TXT reports in `reports/`
- Architecture and workflow diagram in `FLOWCHART.md`
- Presentation outline in `PRESENTATION_OUTLINE.md`

## Scope and limitations
No real account access, credential harvesting, system hash extraction, password guessing or cracking is performed. Linux Shadow and Windows SAM are explained with placeholders only. Hash-format results are heuristic structural hints, not definitive algorithm identification. Time estimates are illustrative and depend on assumptions.
