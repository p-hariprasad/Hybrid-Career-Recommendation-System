import random
import pandas as pd

# Fresher-friendly IT careers
careers = {
    "Software Engineer": {"prog": "High", "creativity": "Low"},
    "Junior Software Engineer": {"prog": "Medium", "creativity": "Low"},
    "Web Developer": {"prog": "Medium", "creativity": "Medium"},
    "Frontend Developer": {"prog": "Medium", "creativity": "High"},
    "Backend Developer": {"prog": "High", "creativity": "Low"},
    "Data Analyst": {"prog": "Medium", "creativity": "Low"},
    "Data Scientist (Junior)": {"prog": "High", "creativity": "Low"},
    "ML Engineer (Junior)": {"prog": "High", "creativity": "Low"},
    "Cloud Engineer (Junior)": {"prog": "High", "creativity": "Low"},
    "DevOps Engineer (Junior)": {"prog": "High", "creativity": "Low"},
    "Cyber Security Analyst": {"prog": "High", "creativity": "Low"},
    "UI/UX Designer": {"prog": "Low", "creativity": "High"},
    "QA Engineer": {"prog": "Medium", "creativity": "Low"}
}

def random_experience():
    r = random.random()
    if r < 0.40:
        return 0
    elif r < 0.70:
        return 1
    elif r < 0.85:
        return 2
    elif r < 0.95:
        return 3
    else:
        return random.randint(4, 5)

rows = []

for _ in range(3000):
    career = random.choice(list(careers.keys()))
    profile = careers[career]
    exp = random_experience()

    row = [
        random.randint(70, 95),          # math_score
        random.randint(70, 95),          # science_score
        profile["prog"],                 # programming_skill
        random.choice(["Medium", "High"]),
        profile["creativity"],           # creativity
        "Technology",                    # interest_area
        exp,                             # experience_years
        career                           # label
    ]

    rows.append(row)

df = pd.DataFrame(rows, columns=[
    "math_score",
    "science_score",
    "programming_skill",
    "communication_skill",
    "creativity",
    "interest_area",
    "experience_years",
    "career"
])

df.to_csv("data/raw_dataset.csv", index=False)

print("✅ Dataset generated successfully (3000 rows)")
