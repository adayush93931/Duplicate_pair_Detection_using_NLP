import streamlit as st
from helper import query_point_creator
import pickle

# Load model
try:
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Ensure 'model.pkl' is in the directory.")

st.header('Duplicate Question Pairs')

# Input fields
q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    if q1 and q2:
        # Preprocess and predict
        query = query_point_creator(q1, q2)
        result = model.predict(query)[0]

        # Display result
        st.header('Duplicate' if result else 'Not Duplicate')
    else:
        st.warning("Please enter both questions to compare.") 
