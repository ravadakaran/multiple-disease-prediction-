"""
MediScan AI - FastAPI Production Backend
Serves modern web dashboard, prediction APIs, and clinical PDF report generator.
"""

import os
import pickle
import warnings
import numpy as np
import pandas as pd
from typing import Dict, Any, List
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from report_generator import generate_pdf_report

warnings.filterwarnings("ignore")

app = FastAPI(
    title="MediScan AI Diagnostic System",
    description="Multi-Disease Machine Learning Risk Screening & Clinical Reporting API",
    version="3.0.0",
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
MODELS_DIR = os.path.join(BASE_DIR, "saved_models")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# ---------------------------------------------------------
# Load Machine Learning Models at Startup
# ---------------------------------------------------------
MODELS = {}


def load_all_models():
    files = {
        "diabetes": "diabetes_model.sav",
        "heart": "heart_disease_model.sav",
        "parkinsons": "parkinsons_model.sav",
        "breast_cancer": "breast_cancer_model.sav",
    }
    for key, filename in files.items():
        path = os.path.join(MODELS_DIR, filename)
        if os.path.exists(path):
            with open(path, "rb") as f:
                MODELS[key] = pickle.load(f)
                print(f"✓ Loaded {key} model from {filename}")
        else:
            print(f"⚠️ Model not found: {filename}")


load_all_models()


def compute_risk_prob(model, df: pd.DataFrame, pred: int) -> float:
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(df)[0]
        return float(probs[1] * 100)
    elif hasattr(model, "decision_function"):
        margin = float(model.decision_function(df)[0])
        prob = 1.0 / (1.0 + np.exp(-margin))
        return float(prob * 100)
    return 85.0 if pred == 1 else 15.0


# ---------------------------------------------------------
# Pydantic Request Schemas
# ---------------------------------------------------------
class ReportRequest(BaseModel):
    disease_name: str
    prediction_text: str
    is_positive: bool
    risk_score: float
    metrics_dict: Dict[str, Any]
    recommendations: List[str]


# ---------------------------------------------------------
# Web Interface Route
# ---------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "loaded_models": list(MODELS.keys()),
    }


# ---------------------------------------------------------
# API Prediction Endpoints
# ---------------------------------------------------------
@app.post("/api/predict/diabetes")
async def predict_diabetes(payload: Dict[str, float]):
    model = MODELS.get("diabetes")
    cols = getattr(
        model,
        "feature_names_in_",
        ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"],
    )
    data = [[payload.get(c, 0.0) for c in cols]]
    input_df = pd.DataFrame(data, columns=cols)

    pred = int(model.predict(input_df)[0])
    prob = compute_risk_prob(model, input_df, pred)
    is_positive = (pred == 1)

    recs = [
        "Schedule an official laboratory HbA1c test and Fasting Plasma Glucose (FPG) test.",
        "Consult an endocrinologist or primary care physician for clinical confirmation.",
        "Review dietary carbohydrate and sugar intake; adopt a regular exercise schedule.",
    ] if is_positive else [
        "Maintain balanced dietary nutrition with whole grains, dietary fiber, and healthy fats.",
        "Engage in at least 150 minutes of aerobic exercise weekly.",
        "Schedule annual preventative metabolic panels.",
    ]

    chart_data = {
        "labels": ["Glucose (mg/dL)", "Blood Pressure", "BMI"],
        "patient_values": [payload.get("Glucose", 85), payload.get("BloodPressure", 66), payload.get("BMI", 26.6)],
        "benchmarks": [100.0, 80.0, 24.9],
    }

    return {
        "disease_name": "Diabetes Mellitus",
        "prediction": pred,
        "is_positive": is_positive,
        "prediction_text": "High Risk: Diabetic Indicators Detected" if is_positive else "Low Risk: Non-Diabetic Profile",
        "risk_score": prob,
        "recommendations": recs,
        "chart_data": chart_data,
    }


@app.post("/api/predict/heart")
async def predict_heart(payload: Dict[str, float]):
    model = MODELS.get("heart")
    cols = getattr(
        model,
        "feature_names_in_",
        ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"],
    )
    data = [[payload.get(c, 0.0) for c in cols]]
    input_df = pd.DataFrame(data, columns=cols)

    pred = int(model.predict(input_df)[0])
    prob = compute_risk_prob(model, input_df, pred)
    is_positive = (pred == 1)

    recs = [
        "Consult a cardiologist for a 12-lead ECG and echocardiogram.",
        "Consider a stress echocardiogram or CT coronary angiogram.",
        "Adopt a low-sodium, heart-healthy Mediterranean diet.",
    ] if is_positive else [
        "Maintain cardiovascular health with 30 minutes of daily aerobic activity.",
        "Keep dietary saturated fats low and avoid tobacco products.",
        "Perform regular annual cardiovascular screenings.",
    ]

    chart_data = {
        "labels": ["Resting BP", "Cholesterol", "Max Heart Rate"],
        "patient_values": [payload.get("trestbps", 130), payload.get("chol", 240), payload.get("thalach", 150)],
        "benchmarks": [120.0, 200.0, 160.0],
    }

    return {
        "disease_name": "Cardiovascular Disease",
        "prediction": pred,
        "is_positive": is_positive,
        "prediction_text": "High Risk: Coronary Heart Disease Indicators" if is_positive else "Low Risk: Healthy Cardiovascular Indicators",
        "risk_score": prob,
        "recommendations": recs,
        "chart_data": chart_data,
    }


@app.post("/api/predict/parkinsons")
async def predict_parkinsons(payload: Dict[str, float]):
    model = MODELS.get("parkinsons")
    cols = getattr(
        model,
        "feature_names_in_",
        [
            "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
            "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
            "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
            "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
        ],
    )
    data = [[payload.get(c, 0.0) for c in cols]]
    input_df = pd.DataFrame(data, columns=cols)

    pred = int(model.predict(input_df)[0])
    prob = compute_risk_prob(model, input_df, pred)
    is_positive = (pred == 1)

    recs = [
        "Consult a neurologist for motor assessment and clinical UPDRS evaluation.",
        "Consider specialized dopamine transporter imaging (DaTscan).",
        "Explore early speech and physical physical therapy interventions.",
    ] if is_positive else [
        "Vocal acoustic dynamics are consistent with standard harmonic stability.",
        "No early acoustic motor tremor markers detected.",
    ]

    chart_data = {
        "labels": ["Mean Freq (Fo)", "HNR (Harmonics)", "PPE (Entropy x100)"],
        "patient_values": [payload.get("MDVP:Fo(Hz)", 197.0), payload.get("HNR", 26.7), payload.get("PPE", 0.08) * 100],
        "benchmarks": [200.0, 25.0, 15.0],
    }

    return {
        "disease_name": "Parkinson's Disease",
        "prediction": pred,
        "is_positive": is_positive,
        "prediction_text": "Elevated Risk: Parkinsonian Vocal Biomarkers Detected" if is_positive else "Low Risk: Normal Acoustic Vocal Profile",
        "risk_score": prob,
        "recommendations": recs,
        "chart_data": chart_data,
    }


@app.post("/api/predict/breast-cancer")
async def predict_breast_cancer(payload: Dict[str, float]):
    model = MODELS.get("breast_cancer")
    cols = [
        "mean radius", "mean texture", "mean perimeter", "mean area",
        "mean smoothness", "mean compactness", "mean concavity",
        "mean concave points", "mean symmetry", "mean fractal dimension",
        "radius error", "texture error", "perimeter error", "area error",
        "smoothness error", "compactness error", "concavity error",
        "concave points error", "symmetry error", "fractal dimension error",
        "worst radius", "worst texture", "worst perimeter", "worst area",
        "worst smoothness", "worst compactness", "worst concavity",
        "worst concave points", "worst symmetry", "worst fractal dimension"
    ]

    # Fill defaults from payload
    row = []
    for c in cols:
        val = payload.get(c)
        if val is None:
            # Fallback estimation from base metric
            base_key = c.replace("worst ", "mean ").replace(" error", "")
            val = payload.get(base_key, 1.0)
        row.append(val)

    input_df = pd.DataFrame([row], columns=cols)
    pred = int(model.predict(input_df)[0])
    prob = compute_risk_prob(model, input_df, pred)
    is_positive = (pred == 1)

    recs = [
        "Urgent referral to a breast surgical oncologist for diagnostic mammography / ultrasound biopsy correlation.",
        "Obtain histopathology review with receptor status testing (ER/PR/HER2).",
    ] if is_positive else [
        "Findings consistent with benign tissue morphology.",
        "Continue routine annual screening mammograms as recommended by physician.",
    ]

    chart_data = {
        "labels": ["Radius", "Texture", "Perimeter (/10)", "Smoothness (x100)"],
        "patient_values": [payload.get("mean radius", 13.5), payload.get("mean texture", 14.3), payload.get("mean perimeter", 87.4) / 10, payload.get("mean smoothness", 0.09) * 100],
        "benchmarks": [14.0, 18.0, 9.0, 10.0],
    }

    return {
        "disease_name": "Breast Cancer Biopsy",
        "prediction": pred,
        "is_positive": is_positive,
        "prediction_text": "Malignant: High Risk Cell Morphology" if is_positive else "Benign: Non-Malignant Cellular Characteristics",
        "risk_score": prob,
        "recommendations": recs,
        "chart_data": chart_data,
    }


# ---------------------------------------------------------
# PDF Diagnostic Report Endpoint
# ---------------------------------------------------------
@app.post("/api/report/pdf")
async def download_pdf_report(req: ReportRequest):
    pdf_bytes = generate_pdf_report(
        disease_name=req.disease_name,
        prediction_text=req.prediction_text,
        is_positive=req.is_positive,
        risk_score=req.risk_score,
        metrics_dict=req.metrics_dict,
        recommendations=req.recommendations,
    )
    filename = f"{req.disease_name.replace(' ', '_')}_Diagnostic_Report.pdf"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
