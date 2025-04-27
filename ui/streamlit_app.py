import streamlit as st
import requests
import json

# MLflow Model API endpoint
API_URL = "http://localhost:5001/invocations"

st.title("🏦 Credit Default Predictor - MLOps Version")

st.markdown("""
Upload a **JSON file** with your input features using the **new MLflow 2.x format**.
The JSON must have **one of these fields**: `"inputs"`, `"instances"`, `"dataframe_split"`, or `"dataframe_records"`.
""")

# Upload JSON file
uploaded_file = st.file_uploader("Upload JSON input (e.g., using 'inputs' field)", type=["json"])

if uploaded_file is not None:
    try:
        input_json = json.load(uploaded_file)
        st.subheader("📋 Uploaded JSON Content:")
        st.json(input_json)

        # Validate input structure
        if not any(key in input_json for key in ["inputs", "instances", "dataframe_split", "dataframe_records"]):
            st.error("❌ Uploaded JSON must contain one of the required fields: 'inputs', 'instances', 'dataframe_split', or 'dataframe_records'.")
        else:
            if st.button("🚀 Send to MLflow Model API"):
                with st.spinner('Sending data to MLflow Model API...'):
                    headers = {"Content-Type": "application/json"}
                    response = requests.post(API_URL, headers=headers, json=input_json)

                if response.status_code == 200:
                    prediction = response.json()
                    st.success("✅ Prediction received!")

                    st.subheader("📈 Prediction Output:")
                    st.json(prediction)
                else:
                    st.error(f"❌ API Error {response.status_code}: {response.text}")

    except json.JSONDecodeError:
        st.error("❌ Failed to decode JSON file. Please upload a valid JSON.")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")