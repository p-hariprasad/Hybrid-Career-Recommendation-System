# ===============================
# Path setup (MUST be at the top)
# ===============================
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# ===============================
# Imports
# ===============================
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from utils.preprocessing import preprocess_data

print(">>> train_model.py STARTED <<<")

# ===============================
# Training function
# ===============================
def train_model():
    print("Loading and preprocessing data...")

    # Load processed data
    X, y = preprocess_data()

    print("Data loaded successfully")
    print("X shape:", X.shape)
    print("y length:", len(y))

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training model...")

    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # ===============================
    # Save model
    # ===============================
    MODEL_DIR = os.path.join(BASE_DIR, "models")
    MODEL_PATH = os.path.join(MODEL_DIR, "career_model.pkl")

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("✅ Model saved successfully at:")
    print(MODEL_PATH)


# ===============================
# Script entry point
# ===============================
if __name__ == "__main__":
    train_model()
