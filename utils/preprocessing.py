# ===============================
# Path setup
# ===============================
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# ===============================
# Imports
# ===============================
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ===============================
# Preprocessing function
# ===============================
def preprocess_data():
    """
    Loads raw dataset, encodes categorical variables,
    and returns X (features) and y (target)
    """

    # Absolute path to dataset
    DATA_PATH = os.path.join(BASE_DIR, "data", "raw_dataset.csv")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # Example preprocessing (adjust to your dataset)
    # ----------------------------------------------
    # Assume last column is target (career)
    X = df.drop("career", axis=1)
    y = df["career"]

    # Encode categorical features
    for col in X.columns:
        if X[col].dtype == "object":
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])

    # Encode target
    target_encoder = LabelEncoder()
    y = target_encoder.fit_transform(y)

    return X, y
def encode_user_profile(profile):
    return [
        profile["math_score"] / 100,
        profile["science_score"] / 100,
        1 if profile["programming_skill"] == "High" else 0.5,
        1 if profile["communication_skill"] == "High" else 0.5,
        1 if profile["creativity"] == "High" else 0.5,
        map_interest(profile["interest_area"]),
        profile["experience_years"] / 10
    ]

def map_interest(area):
    mapping = {
        "Technology": 1,
        "Business": 0.7,
        "Arts": 0.5,
        "Government": 0.6,
        "Engineering": 0.8
    }
    return mapping.get(area, 0.5)
