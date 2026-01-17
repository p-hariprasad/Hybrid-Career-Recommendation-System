SKILL_KEYWORDS = {
    "python": "programming",
    "java": "programming",
    "machine learning": "analytics",
    "data analysis": "analytics",
    "sql": "database",
    "html": "programming",
    "css": "programming",
    "design": "creativity",
    "photoshop": "creativity",
    "communication": "communication",
    "management": "business",
    "marketing": "business"
}

def extract_skills(text):
    found = set()
    for keyword, skill in SKILL_KEYWORDS.items():
        if keyword in text:
            found.add(skill)
    return found
