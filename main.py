"""PCCAS main dashboard - safe synthetic demonstration."""

import json
from pathlib import Path

from modules.password_analyzer import analyze_password
from modules.dictionary_generator import generate_test_dataset
from modules.hash_format_analyzer import analyze_hash_format
from modules.attack_simulator import simulate_resistance
from modules.policy_checker import check_password_policy
from modules.report_generator import generate_report


def run_demo(output_dir="reports"):
    # Synthetic demonstration input only. Never use a real account password.
    sample_password = "N7!vQ2@pL9#xR4$m"
    sample_hash = "a" * 64

    dataset_result = generate_test_dataset()

    password_result = analyze_password(sample_password)
    policy_result = check_password_policy(sample_password)
    hash_result = analyze_hash_format(sample_hash)
    simulation_result = simulate_resistance()

    report_result = generate_report(
        password_analysis=password_result,
        policy_result=policy_result,
        hash_analysis=hash_result,
        simulation_result=simulation_result,
        output_dir=output_dir
    )

    summary = {
        "project": "PCCAS",
        "dataset": dataset_result,
        "password_rating": password_result["rating"],
        "policy_passed": policy_result["passed"],
        "hash_format_guess": hash_result["possible_format"],
        "simulation": simulation_result["simulation"],
        "reports": report_result
    }

    return summary


def main():
    print("=" * 55)
    print(" PCCAS - PASSWORD SECURITY AUDITING TOOLKIT")
    print("=" * 55)
    print("Running safe synthetic security demonstration...\n")

    try:
        result = run_demo()
        print(json.dumps(result, indent=4))
        print("\nPCCAS execution completed.")
    except Exception as error:
        print(f"\nPCCAS ERROR: {error}")
        raise


if __name__ == "__main__":
    main()
