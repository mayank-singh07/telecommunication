import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import load



loaded_model = load("Tele_Communicationn.joblib")

# Initialize session state
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# Define the input fields along with their corresponding input types and conditions
input_columns = {
    'voice.plan': {'type': 'radio', 'options': ['NO', 'YES'], 'text': 'Do you have a voice plan?'},
    'voice.messages': {'type': 'number_input', 'text': 'Enter the number of voice messages'},
    'intl.plan': {'type': 'radio', 'options': ['NO', 'YES'], 'text': 'Do you have an international plan?'},
    'intl.mins': {'type': 'number_input', 'text': 'Enter international duration(min)'},
    'intl.calls': {'type': 'number_input', 'text': 'Enter the number of international calls'},
    'intl.charge': {'type': 'number_input', 'text': 'Enter international charges'},
    'day.mins': {'type': 'number_input', 'text': 'Enter daytime duration(min)'},
    'day.charge': {'type': 'number_input', 'text': 'Enter daytime charges'},
    'eve.mins': {'type': 'number_input', 'text': 'Enter evening duration(min)'},
    'eve.charge': {'type': 'number_input', 'text': 'Enter evening charges'},
    'night.mins': {'type': 'number_input', 'text': 'Enter nighttime duration(min)'},
    'night.charge': {'type': 'number_input', 'text': 'Enter nighttime charges'},
    'customer.calls': {'type': 'number_input', 'text': 'Enter the number of customer calls'},
}
# Create a dictionary to store user input
user_input = {}

# First page layout
st.title("Telecom Churn Prediction")

# Using st.form to wrap the input collection
with st.form("user_input_form"):
    # Collect user inputs on the first page
    for col, input_info in input_columns.items():
        if input_info['type'] == 'number_input':
            user_input[col] = st.number_input(f"{input_info['text']}", value=0, step=1)
        elif input_info['type'] == 'radio':
            # Map 'NO' to 0 and 'YES' to 1
            user_input[col] = 1 if st.radio(f"{input_info['text']}", options=input_info['options'], key=col) == 'YES' else 0

    # Predict button
    if st.form_submit_button("Predict"):
        # Create a DataFrame from user input
        input_df = pd.DataFrame([user_input])
        print(input_df, "input_df")
        # Make prediction
        prediction = loaded_model.predict(pd.DataFrame([user_input]))[0]

        # Set the session state variable to True to show the second page
        st.session_state.show_result = True

# Check if the button to show the second page is clicked
if st.session_state.show_result:
    # Page break
    st.markdown("---")

    # Second page layout
    st.title("Result")

    # Display result with animation or other visualizations
    if prediction == 1:
        st.markdown("This customer is likely to <span style='color:red; font-size:32px;'>CHURN</span>", unsafe_allow_html=True)
        st.image('https://i.gifer.com/3Qxw.gif', caption=" ", width=500)
    else:
        st.markdown("This customer is likely to <span style='color:red; font-size:32px;'>NOT CHURN</span>", unsafe_allow_html=True)
        st.image("https://i.gifer.com/5dk.gif", caption=" ", width=500)
