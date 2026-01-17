import sys
import os

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, render_template, request
from hybrid.hybrid_engine import hybrid_recommendation

# Resume modules
from resume.resume_parser import extract_text
from resume.skill_extractor import extract_skills
from resume.feature_mapper import map_skills_to_features

# Encoding helper
from utils.preprocessing import encode_user_profile

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # ===============================
        # CASE 1: RESUME UPLOAD
        # ===============================
        if "resume" in request.files and request.files["resume"].filename != "":
            resume = request.files["resume"]
            resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
            resume.save(resume_path)

            # Extract text from resume
            resume_text = extract_text(resume_path)

            # Extract skills
            skills = extract_skills(resume_text)

            # Convert skills → user profile
            user_profile = map_skills_to_features(skills)

            # Encode for ML
            encoded_input = encode_user_profile(user_profile)

        # ===============================
        # CASE 2: MANUAL FORM INPUT
        # ===============================
        else:
            user_profile = {
                "math_score": int(request.form["math_score"]),
                "science_score": int(request.form["science_score"]),
                "programming_skill": request.form["programming_skill"],
                "communication_skill": request.form["communication_skill"],
                "creativity": request.form["creativity"],
                "interest_area": request.form["interest_area"],
                "experience_years": int(request.form["experience_years"])
            }

            encoded_input = [
                user_profile["math_score"] / 100,
                user_profile["science_score"] / 100,
                {"Low": 0, "Medium": 1, "High": 2}[user_profile["programming_skill"]],
                {"Low": 0, "Medium": 1, "High": 2}[user_profile["communication_skill"]],
                {"Low": 0, "Medium": 1, "High": 2}[user_profile["creativity"]],
                {
                    "Arts": 0,
                    "Business": 1,
                    "Engineering": 2,
                    "Government": 3,
                    "Technology": 4
                }[user_profile["interest_area"]],
                user_profile["experience_years"]
            ]

        # ===============================
        # HYBRID RECOMMENDATION
        # ===============================
        results, explanations = hybrid_recommendation(
            user_profile,
            encoded_input
        )

        return render_template(
            "result.html",
            results=results,
            explanations=explanations
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
