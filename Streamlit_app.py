# Streamlit_app.py
import streamlit as st

# Set the title of the app
st.title('Name Entry App')

# Create a text input field for the user to enter their name
name = st.text_input("Enter your name:")

# Display a greeting message if the name is entered
if name:
    st.write(f"Hello, {name}!")
