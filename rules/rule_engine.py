def apply_rules(user_profile, scores):
    explanations = []

    # -----------------------------
    # Programming Skill Rules
    # -----------------------------
    if user_profile.get("programming_skill") == "High":
        for role in [
            "Software Engineer",
            "Backend Developer",
            "ML Engineer (Junior)",
            "Data Scientist (Junior)"
        ]:
            if role in scores:
                scores[role] += 0.20  # stronger IT boost

        explanations.append(
            "Strong programming skills increased suitability for core IT roles"
        )

    elif user_profile.get("programming_skill") == "Medium":
        for role in ["Software Engineer", "Backend Developer"]:
            if role in scores:
                scores[role] += 0.10

        explanations.append(
            "Moderate programming skills supported entry-level IT roles"
        )

    # -----------------------------
    # Creativity Rules
    # -----------------------------
    if user_profile.get("creativity") == "High":
        for role in ["UI/UX Designer", "Graphic Designer"]:
            if role in scores:
                scores[role] += 0.15

        explanations.append(
            "High creativity boosted design-oriented career paths"
        )

    # -----------------------------
    # Experience Rules (Freshers Focus)
    # -----------------------------
    exp = user_profile.get("experience_years", 0)

    if exp >= 1:
        for role in [
            "Software Engineer",
            "Backend Developer",
            "DevOps Engineer (Junior)"
        ]:
            if role in scores:
                scores[role] += 0.10

        explanations.append(
            "Relevant experience strengthened practical IT roles"
        )

    elif exp == 0:
        for role in [
            "Software Engineer",
            "Data Scientist (Junior)",
            "QA Engineer"
        ]:
            if role in scores:
                scores[role] += 0.05

        explanations.append(
            "Fresher-friendly roles were prioritized due to limited experience"
        )

    # -----------------------------
    # Reduce Non-IT Dominance
    # -----------------------------
    for non_it_role in ["MBA", "Civil Services"]:
        if non_it_role in scores:
            scores[non_it_role] -= 0.10  # prevent overshadowing IT roles

    # -----------------------------
    # Score Safety Clamp
    # -----------------------------
    for role in scores:
        scores[role] = max(0.0, min(scores[role], 1.0))

    return scores, explanations
