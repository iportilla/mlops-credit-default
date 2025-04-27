import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

# Setup MLflow tracking
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("credit-default-predictions")

data = pd.read_csv('../api/data/raw/april_credit_data.csv')
# data = pd.read_csv('../api/data/raw/may_credit_data.csv')

# CLEAN FIX: Drop 'ID' column if it exists
if 'ID' in data.columns:
    data = data.drop('ID', axis=1)

X = data.drop('default.payment.next.month', axis=1)
y = data['default.payment.next.month']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Create an input example (take 5 samples from training set)
input_example = X_train.sample(5)

with mlflow.start_run():
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="credit_defaults_model_",
        input_example=input_example,
        signature=mlflow.models.infer_signature(X_train, model.predict(X_train))
    )
    mlflow.log_param("algorithm", "GradientBoostingClassifier")
    mlflow.log_param("test_size", 0.2)

    print("✅ Model logged to MLflow (with input example and signature)")# Training script placeholder