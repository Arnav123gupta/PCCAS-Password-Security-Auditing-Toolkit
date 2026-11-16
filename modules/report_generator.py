"""Generate local JSON and text security audit reports."""

import json
from pathlib import Path

def generate_report(
    password_analysis,
    policy_result,
    hash_analysis=None,
    simulation_result=None,
    output_dir="reports"
):
    folder = Path(output_dir)
    folder.mkdir(parents=True, exist_ok=True)

    report = {
        "project": "PCCAS - Password Security Auditing Toolkit",
        "report_type": "Synthetic Security Audit",
        "password_analysis": password_analysis,
        "policy_check": policy_result,
        "hash_analysis": hash_analysis or {},
        "simulation": simulation_result or {}
    }

    json_path = folder / "pccas_report.json"
    text_path = folder / "pccas_report.txt"

    json_path.write_text(
        json.dumps(report, indent=4),
        encoding="utf-8"
    )

    lines = [
        report["project"],
        "=" * 55,
        "Report type: Synthetic Security Audit",
        "",
        "PASSWORD ANALYSIS",
        json.dumps(password_analysis, indent=2),
        "",
        "POLICY CHECK",
        json.dumps(policy_result, indent=2),
        "",
        "HASH FORMAT ANALYSIS",
        json.dumps(report["hash_analysis"], indent=2),
        "",
        "LOCKOUT SIMULATION",
        json.dumps(report["simulation"], indent=2),
        "",
        "Note: This report contains no real account credentials."
    ]

    text_path.write_text("\n".join(lines), encoding="utf-8")

    return {
        "status": "success",
        "json_report": str(json_path),
        "text_report": str(text_path)
    }
