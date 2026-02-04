import re
from typing import Tuple

class RiskClassifier:
    """
    Compliance-Ready Risk Classifier
    Aligned with EU AI Act (2026) Categories
    """

    # EU AI Act: High Risk / Prohibited Patterns
    BIOMETRIC_PATTERNS = [
        (r'\b(face scan|fingerprint|voice print|emotion detection)\b', 1.0), # Prohibited
        (r'\b(identify person|verify identity)\b', 0.9)
    ]

    EMPLOYMENT_PATTERNS = [
        (r'\b(resume screening|hire|fire|candidate ranking)\b', 0.9), # High Risk
        (r'\b(performance review|employee monitoring)\b', 0.85)
    ]

    FINANCIAL_PATTERNS = [
        (r'\b(credit score|loan approval|insurance eligibility)\b', 0.9), # High Risk
        (r'\b(invest|buy stock|crypto)\b', 0.7)
    ]

    def assess_risk(self, query: str) -> Tuple[float, str]:
        query_lower = query.lower()
        risk_score = 0.0
        triggers = []

        all_checks = [
            ("Biometric (Prohibited)", self.BIOMETRIC_PATTERNS),
            ("Employment (High Risk)", self.EMPLOYMENT_PATTERNS),
            ("Financial (High Risk)", self.FINANCIAL_PATTERNS)
        ]

        for category, patterns in all_checks:
            for pattern, weight in patterns:
                if re.search(pattern, query_lower):
                    risk_score = max(risk_score, weight) # Take highest risk found
                    triggers.append(category)

        # Standardize Output
        if risk_score >= 0.9:
            return risk_score, f"CRITICAL: {', '.join(set(triggers))} (Human Loop Required)"
        elif risk_score >= 0.7:
            return risk_score, f"HIGH: {', '.join(set(triggers))} (Audit Trail Active)"

        return 0.1, "LOW: Standard Query"
