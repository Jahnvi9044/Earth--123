import streamlit as st
import numpy as np
import pickle

# Load the model from the file
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title("Earthquake Magnitude Prediction")

latitude = st.number_input("Enter Latitude:", min_value=-90.0, max_value=90.0, value=0.0)
longitude = st.number_input("Enter Longitude:", min_value=-180.0, max_value=180.0, value=0.0)
depth = st.number_input("Enter Depth (km):", min_value=0.0, max_value=700.0, value=0.0)
if st.button("Predict Magnitude"):
    # Prepare the input data
    new_data = np.array([[latitude, longitude, depth]])
    # Predict magnitude
    predicted_mag = model.predict(new_data)
    st.write(f"The predicted magnitude of the earthquake is: {predicted_mag[0]:.2f}")
    
