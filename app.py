import streamlit as st
import pandas as pd
import pickle

# Page title
st.title("Earnings Manipulation Detection App")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Upload Excel file
uploaded_file = st.file_uploader(
    "Upload Excel file",
    type=["xlsx"]
)

if uploaded_file is not None:
    # Read Excel
    df = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data Preview")
    st.dataframe(df)

    # Predict
    predictions = model.predict(df)

    # Add predictions to dataframe
    df["Prediction"] = predictions

    st.subheader("Prediction Results")
    st.dataframe(df)

    # Optional summary
    st.subheader("Summary")
    st.write("Total records:", len(df))
    st.write("Manipulation detected:", (df["Prediction"] == 1).sum())
