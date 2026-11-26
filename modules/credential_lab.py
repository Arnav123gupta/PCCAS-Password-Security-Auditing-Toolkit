"""Mock credential-security demonstrations using synthetic records only."""

def get_synthetic_platform_examples():
    return {
        "linux_shadow_demo": {
            "platform": "Linux shadow-file concept",
            "sample": "SYNTHETIC_USER:$6$EXAMPLE_SALT$NOT_A_REAL_HASH:20000:0:99999:7:::",
            "interpretation": "Illustrative record structure; not read from /etc/shadow."
        },
        "windows_sam_demo": {
            "platform": "Windows SAM concept",
            "sample": "SYNTHETIC_USER:PLACEHOLDER_NTLM_FIELD",
            "interpretation": "Placeholder only; no SAM or SYSTEM hive is accessed."
        }
    }

def assess_mock_credential_risk(records=None):
    """Assess labels in mock records; never accepts or tests real credentials."""
    records = records or [
        {"id": "MOCK-001", "password_class": "common", "mfa": False},  # nosec B105 - mock classification label
        {"id": "MOCK-002", "password_class": "unique", "mfa": True},  # nosec B105 - mock classification label
        {"id": "MOCK-003", "password_class": "reused", "mfa": False},  # nosec B105 - mock classification label
    ]
    results = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each mock record must be a dictionary.")
        kind = record.get("password_class")
        if kind not in {"common", "reused", "unique", "unknown"}:
            raise ValueError("Unsupported synthetic password_class label.")
        mfa = record.get("mfa", False)
        if not isinstance(mfa, bool):
            raise ValueError("mfa must be boolean.")
        risks = []
        if kind == "common":
            risks.append("COMMON_PASSWORD_PATTERN")
        if kind == "reused":
            risks.append("PASSWORD_REUSE")
        if not mfa:
            risks.append("MFA_NOT_ENABLED")
        results.append({
            "mock_id": str(record.get("id", "MOCK-UNKNOWN")),
            "risk_indicators": risks,
            "risk_level": "HIGH" if len(risks) >= 2 else ("MEDIUM" if risks else "LOW")
        })
    return {
        "records_assessed": len(results),
        "results": results,
        "note": "Mock labels only; no credentials, accounts or login endpoints accessed."
    }
