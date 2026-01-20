function openTab(name) {
  document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
  document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));
  document.getElementById(name).classList.add("active");
  event.target.classList.add("active");
}

const FEATURES = {
  diabetes: [
    { key: "Pregnancies", label: "Number of Pregnancies" },
    { key: "Glucose", label: "Plasma Glucose Level" },
    { key: "BloodPressure", label: "Diastolic Blood Pressure (mm Hg)" },
    { key: "SkinThickness", label: "Triceps Skin Fold Thickness (mm)" },
    { key: "Insulin", label: "2-Hour Serum Insulin (mu U/ml)" },
    { key: "BMI", label: "Body Mass Index (BMI)" },
    { key: "DiabetesPedigreeFunction", label: "Diabetes Pedigree Function" },
    { key: "Age", label: "Age (years)" }
  ],

  heart: [
    { key: "age", label: "Age (years)" },
    { key: "sex", label: "Sex (1 = Male, 0 = Female)" },
    { key: "cp", label: "Chest Pain Type" },
    { key: "trestbps", label: "Resting Blood Pressure (mm Hg)" },
    { key: "chol", label: "Serum Cholesterol (mg/dl)" },
    { key: "fbs", label: "Fasting Blood Sugar > 120 mg/dl" },
    { key: "restecg", label: "Resting ECG Result" },
    { key: "thalach", label: "Maximum Heart Rate Achieved" },
    { key: "exang", label: "Exercise Induced Angina" },
    { key: "oldpeak", label: "ST Depression Induced by Exercise" },
    { key: "slope", label: "Slope of Peak Exercise ST Segment" },
    { key: "ca", label: "Number of Major Vessels Colored" },
    { key: "thal", label: "Thalassemia Type" }
  ],

  kidney: [
    { key: "age", label: "Age (years)" },
    { key: "bp", label: "Blood Pressure (mm Hg)" },
    { key: "sg", label: "Specific Gravity" },
    { key: "al", label: "Albumin Level" },
    { key: "su", label: "Sugar Level" },
    { key: "rbc", label: "Red Blood Cells (Normal/Abnormal)" },
    { key: "pc", label: "Pus Cell" },
    { key: "pcc", label: "Pus Cell Clumps" },
    { key: "ba", label: "Bacteria Presence" },
    { key: "bgr", label: "Blood Glucose Random (mg/dl)" },
    { key: "bu", label: "Blood Urea (mg/dl)" },
    { key: "sc", label: "Serum Creatinine (mg/dl)" },
    { key: "sod", label: "Sodium Level (mEq/L)" },
    { key: "pot", label: "Potassium Level (mEq/L)" },
    { key: "hemo", label: "Hemoglobin (g/dl)" },
    { key: "pcv", label: "Packed Cell Volume (%)" },
    { key: "wc", label: "White Blood Cell Count" },
    { key: "rc", label: "Red Blood Cell Count" },
    { key: "htn", label: "Hypertension (Yes/No)" },
    { key: "dm", label: "Diabetes Mellitus (Yes/No)" },
    { key: "cad", label: "Coronary Artery Disease" },
    { key: "appet", label: "Appetite (Good/Poor)" },
    { key: "pe", label: "Pedal Edema" },
    { key: "ane", label: "Anemia" }
  ]
};

function renderForm() {
  const disease = document.getElementById("disease").value;
  const form = document.getElementById("dynamicForm");
  form.innerHTML = "";

  FEATURES[disease].forEach(f => {
    form.innerHTML += `
      <label>${f.label}</label>
      <input type="number" id="${f.key}" required>
    `;
  });
}

renderForm();

async function predict() {
  const disease = document.getElementById("disease").value;
  const payload = {};

  FEATURES[disease].forEach(f => {
    payload[f.key] = Number(document.getElementById(f.key).value);
  });

  document.getElementById("result").innerHTML = "Predicting...";

  const res = await fetch(`/predict/${disease}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const r = await res.json();

  document.getElementById("result").innerHTML = `
    <b>Prediction:</b> ${r.prediction === 1 ? "High Risk" : "Low Risk"}<br>
    <b>Probability:</b> ${r.probability.toFixed(2)}<br>
    <b>Risk Level:</b> ${r.risk}<br><br>
    ${r.ai_explanation}
  `;
}

async function sendChat() {
  const q = document.getElementById("chatInput").value;
  document.getElementById("chatResult").textContent = "Thinking...";

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ messages: [{ role: "user", content: q }] })
  });

  const r = await res.json();
  document.getElementById("chatResult").textContent = r.response;
}
