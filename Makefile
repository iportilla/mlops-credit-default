# Makefile for Credit Default Predictor MLOps Project

.PHONY: all train_april train_may serve ui clean

train_april:
	python training/train.py api/data/raw/april_credit_data.csv

train_may:
	python training/train.py api/data/raw/may_credit_data.csv

serve:
	@echo "Please manually update the RUN ID and serve model using:"
	@echo "mlflow models serve -m mlruns/1/<run_id>/artifacts/credit_defaults_model_ -p 5001"

ui:
	streamlit run ui/streamlit_app.py

clean:
	rm -rf mlruns
	rm -rf __pycache__
