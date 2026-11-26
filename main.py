"""Password Cracking & Credential Attack Suite - synthetic educational demo."""
import json
from modules.password_analyzer import analyze_password
from modules.dictionary_generator import generate_test_dataset, generate_dictionary_demo
from modules.hash_format_analyzer import analyze_hash_format, analyze_sample_catalog
from modules.attack_simulator import simulate_resistance, estimate_resistance
from modules.policy_checker import check_password_policy
from modules.report_generator import generate_report
from modules.credential_lab import get_synthetic_platform_examples, assess_mock_credential_risk

def run_demo(output_dir="reports"):
    sample_password = "N7!vQ2@pL9#xR4$m"  # nosec B105 - synthetic demo fixture
    sample_hash = "a" * 64

    dataset_result = generate_test_dataset()
    dictionary_demo = generate_dictionary_demo()
    password_result = analyze_password(sample_password)
    policy_result = check_password_policy(sample_password)
    hash_result = analyze_hash_format(sample_hash)
    simulation_result = simulate_resistance()
    resistance_estimate = estimate_resistance(length=16, character_pool=94)
    platform_examples = get_synthetic_platform_examples()
    mock_risk = assess_mock_credential_risk()

    additional = {
        "dictionary_demo": dictionary_demo,
        "hash_sample_catalog": analyze_sample_catalog(),
        "resistance_estimate": resistance_estimate,
        "synthetic_platform_examples": platform_examples,
        "mock_credential_risk": mock_risk
    }
    report_result = generate_report(
        password_analysis=password_result,
        policy_result=policy_result,
        hash_analysis=hash_result,
        simulation_result=simulation_result,
        output_dir=output_dir,
        additional_results=additional
    )
    return {
        "project": "PCCAS",
        "dataset": dataset_result,
        "password_rating": password_result["rating"],
        "policy_passed": policy_result["passed"],
        "hash_format_guess": hash_result["possible_format"],
        "simulation": simulation_result["simulation"],
        "additional_modules": additional,
        "reports": report_result
    }

def main():
    print("=" * 64)
    print(" PASSWORD CRACKING & CREDENTIAL ATTACK SUITE")
    print("=" * 64)
    print("Synthetic educational security demonstration only.\n")
    try:
        result = run_demo()
        print(json.dumps(result, indent=4))
        print("\nPCCAS execution completed.")
    except Exception as exc:
        print(f"\nPCCAS ERROR: {exc}")
        raise

if __name__ == "__main__":
    main()
