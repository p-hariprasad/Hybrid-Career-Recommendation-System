def map_skills_to_features(skills):
    return {
        "math_score": 75,
        "science_score": 75,
        "programming_skill": "High" if "programming" in skills else "Medium",
        "communication_skill": "High" if "communication" in skills else "Medium",
        "creativity": "High" if "creativity" in skills else "Low",
        "interest_area": infer_interest(skills),
        "experience_years": infer_experience(skills)
    }

def infer_interest(skills):
    if "analytics" in skills:
        return "Technology"
    if "business" in skills:
        return "Business"
    if "creativity" in skills:
        return "Arts"
    return "Technology"

def infer_experience(skills):
    return min(len(skills), 5)
