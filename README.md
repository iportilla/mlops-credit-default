# 📚 Credit Default Predictor - Local MLOps Project

Welcome to the **Credit Default MLOps Lab**!
This project demonstrates a full local MLOps pipeline using MLflow and Streamlit.

---

## 🚀 Project Objectives

- Install MLflow and set up a local tracking server
- Train two ML models on April and May datasets
- Track model experiments with MLflow
- Serve models automatically with MLflow Models Server
- Test predictions with a Streamlit UI

---

## 🏗️ Project Structure

```
api/
  data/
    raw/
      april_credit_data.csv
      may_credit_data.csv
training/
  train.py
ui/
  streamlit_app.py
  sample_request.json
Makefile
requirements.txt
README.md
```

---

## 🛠️ Quick Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/credit-default-predictor.git
cd credit-default-predictor
```

2. Install Python 3.11 (recommend using pyenv):
```bash
pyenv install 3.11.4
pyenv global 3.11.4
```

3. Install required Python packages:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Commands Cheat Sheet

| Task | Command |
|:---|:---|
| Start MLflow Tracking Server | `mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000` |
| Train April Model | `python training/train.py api/data/raw/april_credit_data.csv` |
| Train May Model | `python training/train.py api/data/raw/may_credit_data.csv` |
| Serve May Model | `mlflow models serve -m mlruns/1/<may_run_id>/artifacts/credit_defaults_model_ -p 5001` |
| Launch Streamlit App | `streamlit run ui/streamlit_app.py` |

---

## 🌎 Architecture Overview

```
Local Machine
   ↓
MLflow Tracking Server (localhost:5000)
   ↓
MLflow Model Server (localhost:5001)
   ↓
Streamlit Frontend (localhost:8501)
```

---

## 🧠 Learning Outcomes

- Full ML model lifecycle management
- Experiment tracking and comparison
- Simple model deployment with REST APIs
- Connecting UIs to live ML models

---

## 📜 License

This project is licensed under the MIT License.

---

# ✨ Happy Predicting! 🚀