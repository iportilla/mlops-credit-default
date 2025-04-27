import streamlit as st
import requests
import json
import pandas as pd

# New MLflow API URL
API_URL = "http://localhost:5001/invocations"

st.title("Credit Default Predictor - MLOps Version")

uploaded_file = st.file_uploader("Upload a sample JSON file (dataframe_split format)", type=["json"])

if uploaded_file is not None:
    try:
        input_json = json.load(uploaded_file)
        st.subheader("Uploaded JSON:")
        st.json(input_json)

        if st.button("Send to MLflow Model API"):
            with st.spinner('Sending data to MLflow Model API...'):
                headers = {"Content-Type": "application/json"}
                response = requests.post(API_URL, headers=headers, json=input_json)

            if response.status_code == 200:
                prediction = response.json()
                st.success("Prediction received!")

                st.subheader("Prediction Output:")
                st.json(prediction)

            else:
                st.error(f"API Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Invalid JSON format: {e}")