function openTab(name) {
  document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
  document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

  document.querySelector(`[onclick="openTab('${name}')"]`).classList.add("active");
  document.getElementById(name).classList.add("active");
}

const FEATURES = {
  diabetes: ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"],
  heart: ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"],
  kidney: ["age","bp","sg","al","su","rbc","pc","pcc","ba","bgr","bu","sc","sod","pot","hemo","pcv","wc","rc","htn","dm","cad","appet","pe","ane"]
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
  FEATURES[disease].forEach(f => data[f] = Number(document.getElementById(f).value));

  document.getElementById("result").innerHTML = "Predicting...";

  const res = await fetch(`/predict/${disease}`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
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
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ messages: [{ role: "user", content: q }] })
  });

  const r = await res.json();
  document.getElementById("chatResult").textContent = r.response;
}
