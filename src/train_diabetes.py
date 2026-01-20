import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix


diabetes = pd.read_csv("data/diabetes.csv")


cols_with_zero_as_missing = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for col in cols_with_zero_as_missing:
    diabetes[col] = diabetes[col].replace(0, diabetes[col].median())


X = diabetes.drop("Outcome", axis=1)
y = diabetes["Outcome"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model = RandomForestClassifier(
    n_estimators=300,
    max_depth=6,
    min_samples_split=10,
    min_samples_leaf=5,
    class_weight={0: 1, 1: 2},
    random_state=42
)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
specificity = tn / (tn + fp)


print("\nDiabetes Model Performance")
print("--------------------------")
print(f"Accuracy     : {accuracy:.3f}")
print(f"Precision    : {precision:.3f}")
print(f"Recall       : {recall:.3f}")
print(f"Specificity  : {specificity:.3f}")


cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print("\nCross-Validation Results")
print("------------------------")
print(f"CV Accuracy Mean : {cv_scores.mean():.3f}")
print(f"CV Accuracy Std  : {cv_scores.std():.3f}")


joblib.dump(model, "models/diabetes_rf_regularized.pkl")

print("\nModel saved as models/diabetes_rf_regularized.pkl")
