from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.inference import predict
from app.llm import generate_explanation
from app.chat import chat_with_ai

app = FastAPI(title="AI Clinical Decision Support System")

# -------------------------------
# Frontend (HTML / CSS / JS)
# -------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# -------------------------------
# Prediction API
# -------------------------------
@app.post("/predict/{disease}")
def predict_disease(disease: str, data: dict):
    pred, prob, risk = predict(disease, data)

    explanation = generate_explanation(
        disease=disease,
        prediction=pred,
        probability=prob,
        risk=risk,
        input_data=data
    )

    return {
        "prediction": pred,
        "probability": prob,
        "risk": risk,
        "ai_explanation": explanation
    }


# -------------------------------
# Chat API
# -------------------------------
@app.post("/chat")
def chat(payload: dict):
    reply = chat_with_ai(payload["messages"])
    return {"response": reply}
