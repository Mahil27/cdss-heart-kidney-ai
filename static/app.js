const FEATURES = {
  diabetes: [
    "Pregnancies","Glucose","BloodPressure","SkinThickness",
    "Insulin","BMI","DiabetesPedigreeFunction","Age"
  ],
  heart: [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal"
  ],
  kidney: [
    "age","bp","sg","al","su","rbc","pc","pcc","ba","bgr",
    "bu","sc","sod","pot","hemo","pcv","wc","rc",
    "htn","dm","cad","appet","pe","ane"
  ]
};

function renderForm() {
  const disease = document.getElementById("disease").value;
  const form = document.getElementById("dynamicForm");
  form.innerHTML = "";

  FEATURES[disease].forEach(f => {
    form.innerHTML += `
      <label>${f}</label>
      <input type="number" id="${f}" required>
    `;
  });
}

renderForm();

async function predict() {
  const disease = document.getElementById("disease").value;
  const data = {};
  FEATURES[disease].forEach(f => {
    data[f] = Number(document.getElementById(f).value);
  });

  document.getElementById("result").textContent = "Predicting...";

  const res = await fetch(`/predict/${disease}`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });

  const json = await res.json();
  document.getElementById("result").textContent =
    `Prediction: ${json.prediction}\nProbability: ${json.probability}\nRisk: ${json.risk}\n\n${json.ai_explanation}`;
}

async function sendChat() {
  const input = document.getElementById("chatInput").value;
  document.getElementById("chatResult").textContent = "Thinking...";

  const res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      messages: [{ role: "user", content: input }]
    })
  });

  const json = await res.json();
  document.getElementById("chatResult").textContent = json.response;
}
