import streamlit as st

st.title("This is a Streamlit website")
st.write("Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time.")
value = st.text_input("Enter a value")
output = value.upper()
output