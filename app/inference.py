import joblib
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


def load_model(filename: str):
    path = MODEL_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Model not found: {path}")
    return joblib.load(path)


MODELS = {
    "diabetes": {
        "model": load_model("diabetes_rf_regularized.pkl"),
        "features": [
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
        ],
    },
    "kidney": {
        "model": load_model("kidney_rf_regularized.pkl"),
        "features": [
            "age", "bp", "bgr", "bu", "sc", "hemo", "wc", "rc",
            "rbc", "pc", "pcc", "ba", "htn", "dm", "cad",
            "appet", "pe", "ane"
        ],
    },
    "heart": {
        "model": load_model("heart_rf_regularized.pkl"),
        "features": [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak",
            "slope", "ca", "thal"
        ],
    },
}


# -------------------------------
# Prediction function
# -------------------------------
def predict(disease: str, data: dict):
    if disease not in MODELS:
        raise ValueError(f"Invalid disease type: {disease}")

    model = MODELS[disease]["model"]
    features = MODELS[disease]["features"]

    try:
        X = np.array([[data[f] for f in features]])
    except KeyError as e:
        raise ValueError(f"Missing required feature: {e}")

    prob = float(model.predict_proba(X)[0][1])

    if prob < 0.3:
        risk = "Low"
        pred = 0
    elif prob < 0.6:
        risk = "Moderate"
        pred = 1
    else:
        risk = "High"
        pred = 1

    return pred, prob, risk
