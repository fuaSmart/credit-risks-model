import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --- PATHS ---
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

# --- LOAD ARTIFACTS ---

try:
    model = joblib.load(MODEL_DIR / "logistic_regression_model.pkl")
    scaler = joblib.load(MODEL_DIR / "scaler.pkl")
    model_columns = joblib.load(MODEL_DIR / "model_columns.pkl")
    st.success("Model artifacts loaded successfully!")
except FileNotFoundError:
    st.error("Model artifacts not found. Please run `python scripts/train.py` first.")
    st.stop()

# --- APP LAYOUT ---
st.title(" BNPL Credit Risk Assessment Dashboard")
st.markdown("Enter transaction details to get a real-time fraud prediction.")

# --- USER INPUT ---
st.sidebar.header("Transaction Features")


def user_input_features():

    amount = st.sidebar.number_input('Transaction Amount', min_value=0.0, value=10000.0, step=100.0)
    recency = st.sidebar.slider('Days Since Last Transaction (Recency)', 1, 365, 10)
    frequency = st.sidebar.slider('Customer Transaction Frequency', 1, 100, 5)
    monetary_mean = st.sidebar.number_input('Customer Average Transaction Value', min_value=0.0, value=5000.0, step=100.0)
    channel_id = st.sidebar.selectbox('Channel ID', ['ChannelId_1', 'ChannelId_2', 'ChannelId_3', 'ChannelId_5'])
    product_category = st.sidebar.selectbox('Product Category', ['airtime', 'utility_bill', 'retail', 'data_bundles', 'financial_services', 'tv'])

    data = {
        'Amount': amount,
        'Value': abs(amount), 
        'Recency': recency,
        'Frequency': frequency,
        'MonetaryMean': monetary_mean,
        'ChannelId': channel_id,
        'ProductCategory': product_category

    }
    return data

input_data = user_input_features()

# --- PREDICTION LOGIC ---
if st.button('Assess Transaction Risk'):

    input_df = pd.DataFrame([input_data])
    

    input_encoded = pd.get_dummies(input_df).reindex(columns=model_columns, fill_value=0)
    

    input_scaled = scaler.transform(input_encoded)
    

    prediction_proba = model.predict_proba(input_scaled)[:, 1]
    prediction = model.predict(input_scaled)

    # --- DISPLAY RESULTS ---
    st.subheader('Risk Assessment Result')
    
    probability_value = prediction_proba[0]
    

    if prediction[0] == 1:
        st.metric(label="Risk Prediction", value="High Risk (Fraud Likely)", delta=f"{probability_value:.2%} Probability")
        st.warning("Recommendation: This transaction should be flagged for manual review.")
    else:
        st.metric(label="Risk Prediction", value="Low Risk (Likely Legitimate)", delta=f"-{probability_value:.2%} Probability")
        st.success("Recommendation: This transaction can be automatically approved.")
        

    with st.expander("See Prediction Details"):
        st.write("The prediction is based on the features you provided. The model identified the following risk factors:")
        st.json(input_data)
        st.write("The final fraud probability is calculated based on our trained Logistic Regression model.")