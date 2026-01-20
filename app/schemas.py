from pydantic import BaseModel
from typing import List

# ================= CHAT =================

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatInput(BaseModel):
    messages: List[ChatMessage]


# ================= DIABETES =================

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# ================= KIDNEY =================

class KidneyInput(BaseModel):
    age: int
    bp: int
    bgr: float
    bu: float
    sc: float
    hemo: float
    wc: float
    rc: float
    rbc: int
    pc: int
    pcc: int
    ba: int
    htn: int
    dm: int
    cad: int
    appet: int
    pe: int
    ane: int


# ================= HEART =================

class HeartInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int
