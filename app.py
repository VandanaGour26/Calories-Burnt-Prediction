import streamlit as st
import pickle
import pandas as pd
import numpy as np

#load the model
model_path="pipeline.pkl"
with open(model_path,'rb') as file:
    pipeline_saved=pickle.load(file)

#streamlit page configuration
st.set_page_config(page_title="Calories_prediction",page_icon="c",layout='centered')

#add custom css for styling
page_element="""
<style>
 /* ✅ Background image */
[data-testid="stAppViewContainer"] {
  background-image: url("https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
  background-size: cover;
  background-position: center;
}

/* ✅ Input styling (Text, Number, Select, etc.) */
 
div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"]
 {
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); 
  border-radius: 8px;
  padding: 8px;
  transition: 0.3s;
  font-size: 20px;
  background-color: rgba(255, 255, 255, 0.1) ;
}

div[data-baseweb="select"] > div {
  color: blue !important; /* ✅ Make dropdown options like 'Male'/'Female' visible */
  font-weight: bold;
}

/* ✅ Dropdown option styling */
.css-1wa3eu0-placeholder,
.css-qc6sy-singleValue {
  color: blue !important;
  font-weight: bold;
}

/* ✅ Markdown text */
div[data-testid="stMarkdownContainer"] {
  font-size: 18px;
  font-weight: bold;
  color: green;    
}

/* ✅ Buttons */
div[data-testid="stButton"] > button {
  background-color: red !important;   
  color: black !important;   
  border-radius: 8px;   
  padding: 10px 20px;
  font-size: 18px;
  font-weight: bold;
  border: none;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
  transition: 0.3s;
}
div[data-testid="stButton"] > button:hover {
  background-color: lighter!important;   
  box-shadow: 3px 3px 12px rgba(255, 0, 0, 0.5);  
}

/* ✅ Fonts and global color */
* {
  font-family: 'Pacifico';
  color: darkorange;
}

/* ✅ Fancy heading */
.fancy-heading {
  background-color: pink;  
  padding: 10px;
  border-radius: 10px;
  font-size: 32px;
  text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
  text-align: center;
  color: darkblue;
  font-weight: bold;
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
  margin: 8px;
}
</style>
"""

st.markdown(page_element,unsafe_allow_html=True)

st.title("Calories Burnt Prediction")
st.write("Enter your exercise details to predict how much calories you burnt")

# Gender=st.
# Gender,Age,Height,Weight,Duration,Heart_rate,Body_temperature
with st.form(key='calorie_form'):
    gender = st.selectbox('Gender', ["male", " female"])
    age = st.number_input('Age', min_value=0)
    height = st.number_input('Height (in cm)', min_value=0)
    weight = st.number_input('Weight (in kg)', min_value=0)
    duration = st.number_input('Duration of Exercise (in minutes)', min_value=0)
    heart_rate = st.number_input('Heart Rate (bpm)', min_value=0)
    body_temp = st.number_input('Body Temperature (°C)', min_value=0.0, format="%.1f")

    submit_button = st.form_submit_button(label='Predict')

# Run prediction when form is submitted
if submit_button:
    # Create input DataFrame (keep same order as during training)
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }])

    # Predict
    prediction = pipeline_saved.predict(input_df)
    st.success(f"Estimated Calories Burnt: {prediction[0]:.2f} calories")