import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import joblib
import numpy as np

# Career labels (must match training order)
CAREER_LABELS = [
    "Data Scientist",
    "Software Engineer",
    "MBA",
    "Web Developer",
    "Mechanical Engineer",
    "Civil Services",
    "Graphic Designer"
]

def predict_career(user_input):
    """
    user_input: list of numeric features after encoding
    """

    # Load trained model
    model = joblib.load("models/career_model.pkl")

    # Convert input to numpy array
    input_array = np.array(user_input).reshape(1, -1)

    # Predict probabilities
    probabilities = model.predict_proba(input_array)[0]

    # Map probabilities to career labels
    result = dict(zip(CAREER_LABELS, probabilities))

    return result
