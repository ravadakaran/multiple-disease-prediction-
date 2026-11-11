"""
Model Training & Serialization Pipeline for Multiple Disease Prediction System.
Re-trains the 3 machine learning models using the local datasets and saves them
into the `saved_models/` directory using the current scikit-learn environment.
"""

import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
MODELS_DIR = os.path.join(BASE_DIR, "saved_models")
os.makedirs(MODELS_DIR, exist_ok=True)


def train_diabetes():
    print("=" * 50)
    print("Training Diabetes Prediction Model (SVM)...")
    data_path = os.path.join(DATASET_DIR, "diabetes.csv")
    df = pd.read_csv(data_path)

    X = df.drop(columns="Outcome", axis=1)
    Y = df["Outcome"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, stratify=Y, random_state=2
    )

    classifier = svm.SVC(kernel="linear", probability=True, random_state=2)
    classifier.fit(X_train, Y_train)

    train_acc = accuracy_score(Y_train, classifier.predict(X_train))
    test_acc = accuracy_score(Y_test, classifier.predict(X_test))

    print(f"Training Accuracy : {train_acc * 100:.2f}%")
    print(f"Test Accuracy     : {test_acc * 100:.2f}%")

    out_path = os.path.join(MODELS_DIR, "diabetes_model.sav")
    with open(out_path, "wb") as f:
        pickle.dump(classifier, f)
    print(f"Saved: {out_path}\n")


def train_heart():
    print("=" * 50)
    print("Training Heart Disease Model (Logistic Regression)...")
    data_path = os.path.join(DATASET_DIR, "heart.csv")
    df = pd.read_csv(data_path)

    X = df.drop(columns="target", axis=1)
    Y = df["target"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, stratify=Y, random_state=2
    )

    model = LogisticRegression(max_iter=1000, random_state=2)
    model.fit(X_train, Y_train)

    train_acc = accuracy_score(Y_train, model.predict(X_train))
    test_acc = accuracy_score(Y_test, model.predict(X_test))

    print(f"Training Accuracy : {train_acc * 100:.2f}%")
    print(f"Test Accuracy     : {test_acc * 100:.2f}%")

    out_path = os.path.join(MODELS_DIR, "heart_disease_model.sav")
    with open(out_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Saved: {out_path}\n")


def train_parkinsons():
    print("=" * 50)
    print("Training Parkinson's Disease Model (SVM)...")
    data_path = os.path.join(DATASET_DIR, "parkinsons.csv")
    df = pd.read_csv(data_path)

    X = df.drop(columns=["name", "status"], axis=1)
    Y = df["status"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=2
    )

    model = svm.SVC(kernel="linear", probability=True, random_state=2)
    model.fit(X_train, Y_train)

    train_acc = accuracy_score(Y_train, model.predict(X_train))
    test_acc = accuracy_score(Y_test, model.predict(X_test))

    print(f"Training Accuracy : {train_acc * 100:.2f}%")
    print(f"Test Accuracy     : {test_acc * 100:.2f}%")

    out_path = os.path.join(MODELS_DIR, "parkinsons_model.sav")
    with open(out_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Saved: {out_path}\n")


def train_breast_cancer():
    print("=" * 50)
    print("Training Breast Cancer Biopsy Model (Random Forest Pipeline)...")
    data_path = os.path.join(DATASET_DIR, "breast_cancer.csv")
    df = pd.read_csv(data_path)

    X = df.drop(columns="target")
    Y = df["target"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, stratify=Y, random_state=42
    )

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(n_estimators=100, random_state=42)),
    ])
    pipeline.fit(X_train, Y_train)

    train_acc = accuracy_score(Y_train, pipeline.predict(X_train))
    test_acc = accuracy_score(Y_test, pipeline.predict(X_test))

    print(f"Training Accuracy : {train_acc * 100:.2f}%")
    print(f"Test Accuracy     : {test_acc * 100:.2f}%")

    out_path = os.path.join(MODELS_DIR, "breast_cancer_model.sav")
    with open(out_path, "wb") as f:
        pickle.dump(pipeline, f)
    print(f"Saved: {out_path}\n")


if __name__ == "__main__":
    train_diabetes()
    train_heart()
    train_parkinsons()
    train_breast_cancer()
    print("All 4 models successfully trained and serialized!")

