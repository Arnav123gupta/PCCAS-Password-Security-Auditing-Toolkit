import json
from main import run_demo


def test_full_project_integration(tmp_path):
    result = run_demo(output_dir=tmp_path)

    assert result["project"] == "PCCAS"
    assert result["dataset"]["status"] == "success"
    assert result["policy_passed"] is True
    assert result["reports"]["status"] == "success"

    report = json.loads(
        (tmp_path / "pccas_report.json").read_text(encoding="utf-8")
    )
    assert "password_analysis" in report
    assert "simulation" in report
