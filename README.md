# MediScan AI — Multiple Disease Diagnostic & Risk Analytics Platform 🧑‍⚕️

A modern, fast, full-stack healthcare web application built with **FastAPI**, **Tailwind CSS**, and **Scikit-Learn**. It replaces slow Python dashboard reloads with instantaneous, asynchronous single-page risk screening, interactive benchmark charts, and automated clinical PDF report generation.

---

## 🚀 Key Advantages Over Streamlit

- **⚡ Blazing Fast Asynchronous Architecture**: Powered by **FastAPI** & **Uvicorn** with sub-20ms inference latency.
- **🚫 Zero Page Reloads**: Clean, modern Single Page Application (SPA) powered by Tailwind CSS and JavaScript `fetch()` calls. Form submissions update results instantly without refreshing the page.
- **📑 Automatic Interactive Swagger API Documentation**: Fully documented REST endpoints accessible at `/docs` (Swagger UI) and `/redoc`.
- **📊 Dynamic Visual Analytics**: Real-time Chart.js risk indices and patient-vs-normal clinical benchmark comparisons.
- **📥 One-Click Medical Diagnostic Reports (PDF)**: Generates formatted clinical screening PDF summaries on demand.
- **🩺 4 Supported Disease Screening Modules**:
  1. **Diabetes Mellitus** (Pima Indians Dataset)
  2. **Cardiovascular / Coronary Heart Disease** (Cleveland Heart Dataset)
  3. **Parkinson's Disease Vocal Biomarkers** (Oxford Acoustic Voice Dataset)
  4. **Breast Cancer Biopsy Staging** (Fine Needle Aspirate Cell Nuclei Classification)

---

## 🏃 Quick Start

### 1. Set Up Environment & Install Dependencies

```bash
# Clone the repository
git clone https://github.com/ravadakaran/multiple-disease-prediction-.git
cd multiple-disease-prediction-

# Create and activate virtual environment
python -m venv .venv

# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Windows (Command Prompt):
.\.venv\Scripts\activate.bat
# Linux / macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Verify Models & Run Test Suite

```bash
python test_app.py
```

### 3. Launch the Server

Double-click `start_server.bat` or run:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser at:
* **Web Dashboard**: **[http://localhost:8000](http://localhost:8000)**
* **Interactive API Docs (Swagger UI)**: **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 📁 Repository Structure

```
├── main.py                        # FastAPI production web server & API routes
├── templates/
│   └── index.html                 # Modern Tailwind CSS + Chart.js Single Page App
├── report_generator.py            # PDF clinical diagnostic report generator (fpdf2)
├── chart_utils.py                 # Plotly visual gauge utilities
├── train_models.py                # Standalone model training & serialization pipeline
├── test_app.py                    # Automated test suite for all models
├── start_server.bat               # 1-click Windows launcher
├── requirements.txt               # Project dependencies
│
├── dataset/                       # Clinical benchmark datasets
│   ├── diabetes.csv
│   ├── heart.csv
│   ├── parkinsons.csv
│   └── breast_cancer.csv
│
├── saved_models/                  # Trained serialized models (.sav)
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinsons_model.sav
│   └── breast_cancer_model.sav
│
└── colab_files_to_train_models/   # Training and EDA Jupyter notebooks
```

---

## ⚠️ Medical Disclaimer
This software is developed strictly for research, educational, and screening demonstration purposes. It does not replace certified professional clinical consultations or laboratory diagnostic tests.
