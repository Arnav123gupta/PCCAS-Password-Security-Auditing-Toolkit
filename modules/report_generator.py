"""Generate local JSON and text security audit reports."""
import json
from pathlib import Path

def generate_report(password_analysis, policy_result, hash_analysis=None,
                    simulation_result=None, output_dir="reports",
                    additional_results=None):
    folder = Path(output_dir)
    folder.mkdir(parents=True, exist_ok=True)
    report = {
        "project": "Password Cracking & Credential Attack Suite",
        "report_type": "Synthetic Educational Security Assessment",
        "password_analysis": password_analysis,
        "policy_check": policy_result,
        "hash_analysis": hash_analysis or {},
        "simulation": simulation_result or {},
        "additional_results": additional_results or {},
        "safety_scope": (
            "Synthetic data only; no real account credentials are extracted, "
            "guessed, cracked, or used against accounts."
        )
    }
    json_path = folder / "pccas_report.json"
    text_path = folder / "pccas_report.txt"
    json_path.write_text(json.dumps(report, indent=4), encoding="utf-8")
    sections = [
        report["project"], "=" * 60,
        "Report type: Synthetic Educational Security Assessment",
        "",
        "PASSWORD ANALYSIS", json.dumps(password_analysis, indent=2),
        "", "POLICY CHECK", json.dumps(policy_result, indent=2),
        "", "HASH FORMAT ANALYSIS", json.dumps(report["hash_analysis"], indent=2),
        "", "SIMULATION", json.dumps(report["simulation"], indent=2),
        "", "ADDITIONAL RESULTS", json.dumps(report["additional_results"], indent=2),
        "", "SAFETY NOTE", report["safety_scope"]
    ]
    text_path.write_text("\n".join(sections), encoding="utf-8")
    return {"status": "success", "json_report": str(json_path),
            "text_report": str(text_path)}
