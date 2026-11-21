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


def test_main_prints_success_message(monkeypatch, capsys):
    import main

    monkeypatch.setattr(
        main,
        "run_demo",
        lambda: {"project": "PCCAS", "status": "success"}
    )
    main.main()
    output = capsys.readouterr().out
    assert "PCCAS execution completed." in output


def test_main_reports_and_reraises_error(monkeypatch, capsys):
    import pytest
    import main

    def fail_demo():
        raise RuntimeError("controlled test error")

    monkeypatch.setattr(main, "run_demo", fail_demo)

    with pytest.raises(RuntimeError, match="controlled test error"):
        main.main()

    assert "PCCAS ERROR" in capsys.readouterr().out
