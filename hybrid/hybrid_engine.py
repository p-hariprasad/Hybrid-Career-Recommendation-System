import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ml.predict import predict_career
from rules.rule_engine import apply_rules
import math


def softmax(scores):
    """
    Convert raw scores into probability-like confidence values
    """
    exp_scores = {}
    total = 0.0

    for role, score in scores.items():
        exp_scores[role] = math.exp(score)
        total += exp_scores[role]

    for role in exp_scores:
        exp_scores[role] = exp_scores[role] / total

    return exp_scores


def hybrid_recommendation(user_profile, encoded_input):
    """
    user_profile: dictionary (manual or resume-derived)
    encoded_input: numeric vector for ML model
    """

    # -----------------------------
    # Step 1: ML Prediction
    # -----------------------------
    ml_scores = predict_career(encoded_input)
    # Example: {"Software Engineer": 0.42, "MBA": 0.31, ...}

    # -----------------------------
    # Step 2: Rule-based Adjustment
    # -----------------------------
    adjusted_scores, explanations = apply_rules(
        user_profile,
        ml_scores
    )

    # -----------------------------
    # Step 3: Normalize with Softmax
    # -----------------------------
    final_scores = softmax(adjusted_scores)

    # -----------------------------
    # Step 4: Get Top-3 Careers
    # -----------------------------
    top_careers = sorted(
        final_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return top_careers, explanations
