import json
from modules.report_generator import generate_report


def test_report_files_are_created(tmp_path):
    result = generate_report(
        password_analysis={"rating": "STRONG"},
        policy_result={"passed": True},
        hash_analysis={"possible_format": "SHA-256"},
        simulation_result={"simulation": "LOCKOUT_POLICY"},
        output_dir=tmp_path
    )

    assert result["status"] == "success"

    json_file = tmp_path / "pccas_report.json"
    text_file = tmp_path / "pccas_report.txt"

    assert json_file.exists()
    assert text_file.exists()

    data = json.loads(json_file.read_text(encoding="utf-8"))
    assert data["password_analysis"]["rating"] == "STRONG"


def test_report_contains_safety_note(tmp_path):
    generate_report(
        password_analysis={},
        policy_result={},
        output_dir=tmp_path
    )

    content = (tmp_path / "pccas_report.txt").read_text(encoding="utf-8")
    assert "no real account credentials" in content
