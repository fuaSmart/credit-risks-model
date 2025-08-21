
import pytest
from pathlib import Path
import joblib

MODEL_PATH = Path("models/logistic_regression_model.pkl")
SCALER_PATH = Path("models/scaler.pkl")

def test_training_script_creates_artifacts():
 
    assert MODEL_PATH.exists(), "Model file was not created by the training script."
    assert SCALER_PATH.exists(), "Scaler file was not created by the training script."

def test_saved_model_can_be_loaded():

    model = joblib.load(MODEL_PATH)
    assert hasattr(model, 'predict'), "Loaded object is not a valid model."