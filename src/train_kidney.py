import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix


kidney = pd.read_csv("data/kidney_disease.csv")

kidney = kidney.drop(columns=["id"])

kidney["classification"] = kidney["classification"].astype(str).str.strip()
kidney = kidney[kidney["classification"].isin(["ckd", "notckd"])]
kidney["classification"] = kidney["classification"].map({"ckd": 1, "notckd": 0})


num_cols = [
    "age", "bp", "sg", "al", "su", "bgr", "bu", "sc",
    "sod", "pot", "hemo", "pcv", "wc", "rc"
]

cat_cols = [
    "rbc", "pc", "pcc", "ba", "htn", "dm",
    "cad", "appet", "pe", "ane"
]


X = kidney.drop(columns=["classification"])
y = kidney["classification"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42,
    stratify=y
)


for col in num_cols:
    X_train[col] = pd.to_numeric(X_train[col], errors="coerce")
    median = X_train[col].median()
    X_train[col] = X_train[col].fillna(median)

    X_test[col] = pd.to_numeric(X_test[col], errors="coerce")
    X_test[col] = X_test[col].fillna(median)


for col in cat_cols:
    mode = X_train[col].mode()[0]

    X_train[col] = X_train[col].fillna(mode)
    X_test[col] = X_test[col].fillna(mode)

    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col])
    X_test[col] = le.transform(X_test[col])


model = RandomForestClassifier(
    n_estimators=300,
    max_depth=7,
    min_samples_split=8,
    min_samples_leaf=4,
    random_state=42
)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
specificity = tn / (tn + fp)


print("\nKidney Disease Model Performance")
print("-------------------------------")
print(f"Accuracy     : {accuracy:.3f}")
print(f"Precision    : {precision:.3f}")
print(f"Recall       : {recall:.3f}")
print(f"Specificity  : {specificity:.3f}")


cv_scores = cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="accuracy"
)


print("\nCross-Validation Results")
print("------------------------")
print(f"CV Accuracy Mean : {cv_scores.mean():.3f}")
print(f"CV Accuracy Std  : {cv_scores.std():.3f}")


joblib.dump(model, "models/kidney_rf_regularized.pkl")

print("\nModel saved as models/kidney_rf_regularized.pkl")
