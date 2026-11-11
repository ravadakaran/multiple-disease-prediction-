"""
Automated Test Suite for Multiple Disease Prediction System.
Tests model integrity, feature alignment, and sample prediction inferences.
"""

import os
import pickle
import pandas as pd

def test_models():
    working_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_models")
    
    # 1. Verify model files exist
    models_to_check = [
        "diabetes_model.sav",
        "heart_disease_model.sav",
        "parkinsons_model.sav",
        "breast_cancer_model.sav"
    ]
    for m in models_to_check:
        path = os.path.join(working_dir, m)
        assert os.path.exists(path), f"Missing model file: {path}"
        print(f"✓ Found {m}")

    # 2. Test Diabetes Model
    with open(os.path.join(working_dir, "diabetes_model.sav"), "rb") as f:
        diabetes_model = pickle.load(f)
    
    d_healthy = [1, 85.0, 66.0, 29.0, 0.0, 26.6, 0.351, 31]
    d_risk = [6, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50]
    df_dh = pd.DataFrame([d_healthy], columns=diabetes_model.feature_names_in_)
    df_dr = pd.DataFrame([d_risk], columns=diabetes_model.feature_names_in_)
    assert diabetes_model.predict(df_dh)[0] == 0, "Diabetes healthy sample prediction failed!"
    assert diabetes_model.predict(df_dr)[0] == 1, "Diabetes risk sample prediction failed!"
    print("✓ Diabetes model: healthy (0) and diabetic (1) predictions verified.")

    # 3. Test Heart Disease Model
    with open(os.path.join(working_dir, "heart_disease_model.sav"), "rb") as f:
        heart_model = pickle.load(f)

    h_healthy = [67, 1, 0, 160.0, 286.0, 0, 0, 108.0, 1, 1.5, 1, 3, 2]
    h_risk = [63, 1, 3, 145.0, 233.0, 1, 0, 150.0, 0, 2.3, 0, 0, 1]
    df_hh = pd.DataFrame([h_healthy], columns=heart_model.feature_names_in_)
    df_hr = pd.DataFrame([h_risk], columns=heart_model.feature_names_in_)
    assert heart_model.predict(df_hh)[0] == 0, "Heart healthy sample prediction failed!"
    assert heart_model.predict(df_hr)[0] == 1, "Heart risk sample prediction failed!"
    print("✓ Heart Disease model: low risk (0) and high risk (1) predictions verified.")

    # 4. Test Parkinson's Disease Model
    with open(os.path.join(working_dir, "parkinsons_model.sav"), "rb") as f:
        parkinsons_model = pickle.load(f)

    p_healthy = [
        197.076, 206.896, 192.055, 0.00289, 0.00001, 0.00166, 0.00168, 0.00498,
        0.01098, 0.097, 0.00563, 0.0068, 0.00802, 0.01689, 0.00339, 26.775,
        0.422229, 0.741367, -7.3483, 0.177551, 1.743867, 0.085569
    ]
    p_risk = [
        119.992, 157.302, 74.997, 0.00784, 0.00007, 0.00370, 0.00554, 0.01109,
        0.04374, 0.426, 0.02182, 0.0313, 0.02971, 0.06545, 0.02211, 21.033,
        0.414783, 0.815285, -4.813031, 0.266482, 2.301442, 0.284654
    ]
    df_ph = pd.DataFrame([p_healthy], columns=parkinsons_model.feature_names_in_)
    df_pr = pd.DataFrame([p_risk], columns=parkinsons_model.feature_names_in_)
    assert parkinsons_model.predict(df_ph)[0] == 0, "Parkinson's healthy sample prediction failed!"
    assert parkinsons_model.predict(df_pr)[0] == 1, "Parkinson's risk sample prediction failed!"
    print("✓ Parkinson's Disease model: healthy voice (0) and Parkinson's (1) predictions verified.")

    # 5. Test Breast Cancer Model
    with open(os.path.join(working_dir, "breast_cancer_model.sav"), "rb") as f:
        bc_model = pickle.load(f)
    
    df_bc = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset", "breast_cancer.csv"))
    sample_benign = df_bc[df_bc['target'] == 0].drop(columns='target').iloc[0:1]
    sample_malignant = df_bc[df_bc['target'] == 1].drop(columns='target').iloc[0:1]
    assert bc_model.predict(sample_benign)[0] == 0, "Breast cancer benign sample prediction failed!"
    assert bc_model.predict(sample_malignant)[0] == 1, "Breast cancer malignant sample prediction failed!"
    print("✓ Breast Cancer model: benign (0) and malignant (1) predictions verified.")

    print("\nAll 4 disease models passed automated test verification successfully!")

if __name__ == "__main__":
    test_models()
