🩺 AI Clinical Decision Support System (CDSS)

An end-to-end AI-powered Clinical Decision Support System for predicting Heart Disease, Diabetes, and Chronic Kidney Disease, integrated with an AI medical chatbot to enhance interpretability and decision support.

🔗 Live Application:
👉 https://cdss-heart-kidney-ai.onrender.com

📌 Project Overview

Clinical Decision Support Systems (CDSS) assist healthcare professionals by providing data-driven insights at the point of care.
This project combines:

Machine Learning–based disease risk prediction

Explainable AI (XAI) via LLM-generated explanations

A full-stack web application

Cloud deployment with Docker

The system is designed to support medical decision-making, not replace healthcare professionals.

🚀 Key Features
🧠 Disease Risk Prediction

Heart Disease Prediction

Diabetes Prediction

Chronic Kidney Disease Prediction

Probability-based risk classification (Low / Moderate / High)

Robust ML inference via trained Random Forest models

🤖 AI Explainability Layer

AI-generated medical explanations for each prediction

Rule-constrained responses (health-only)

Bullet-point format for clarity

Powered by Groq LLM

💬 AI Medical Chatbot

Answers health-related questions only

Enforces medical-scope safety

Designed for patient education and clarification

🌐 Web Application

Clean, professional medical-grade UI

Human-readable feature labels

Mobile-responsive design

Prediction and Chat separated into tabs

🛠️ Technology Stack
Machine Learning

Python

Scikit-learn

Random Forest Classifier

Joblib (model persistence)

Backend

FastAPI (high-performance API)

Pydantic

Uvicorn

Frontend

HTML5

CSS3

JavaScript (Vanilla)

AI / NLP

Groq API

Large Language Models (LLMs)

DevOps & Deployment

Docker

Render (Cloud Hosting)

GitHub

🔬 Machine Learning Models & Performance
❤️ Heart Disease Prediction

Model: Random Forest Classifier

Objective: Binary classification

Performance

Accuracy     : 94.6%
Precision    : 92.7%
Recall       : 97.1%
Specificity  : 92.0%


Cross-Validation

Mean CV Accuracy : 93.1%


High recall ensures minimal false negatives, which is critical in cardiac risk assessment.

🩸 Diabetes Prediction

Model: Regularized Random Forest

Objective: Binary classification

Performance

Accuracy     : 75.3%
Precision    : 61.8%
Recall       : 77.8%
Specificity  : 74.0%


Cross-Validation

Mean CV Accuracy : 76.7%
Std Deviation   : 3.8%


Performance reflects real-world class imbalance, prioritizing recall for early detection.

🧪 Chronic Kidney Disease Prediction

Model: Random Forest Classifier

Objective: CKD vs Non-CKD classification

Performance

Accuracy     : 99.4%
Precision    : 99.0%
Recall       : 100.0%
Specificity  : 98.3%


Cross-Validation

Mean CV Accuracy : 96.7%
Std Deviation   : 1.0%


Near-perfect recall ensures no CKD cases are missed during inference.

📈 Evaluation Strategy

Models were evaluated using:

Accuracy

Precision

Recall (Sensitivity)

Specificity

k-Fold Cross-Validation

This ensures robust generalization and minimizes overfitting.

🧠 Explainable AI (XAI)

To improve trust and interpretability:

Each prediction is paired with an AI-generated explanation

Explanations are constrained by strict medical rules

Avoids hallucinations and non-medical content

Bridges the gap between black-box ML and human understanding

🏗️ Project Structure
cdss-heart-kidney-ai/
│
├── app/              # FastAPI backend (API, ML inference, AI logic)
├── models/           # Trained ML models (.pkl)
├── templates/        # HTML templates
├── static/           # CSS & JavaScript
├── src/              # Model training scripts (research)
├── Dockerfile
├── requirements.txt
└── README.md

⚙️ Running Locally

git clone https://github.com/YOUR_USERNAME/cdss-heart-kidney-ai.git
cd cdss-heart-kidney-ai

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\Activate

pip install -r requirements.txt
uvicorn app.main:app --reload


Open:

http://localhost:8000

http://localhost:8000/docs

🔐 Environment Variables

Set the following variable (locally or in Render):

GROQ_API_KEY=your_groq_api_key


API keys are never committed to the repository.

⚠️ Disclaimer

This project is intended for educational and research purposes only.
It does not replace professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare professional.