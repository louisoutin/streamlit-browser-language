import streamlit as st
from language_detection import detect_browser_language

st.set_page_config(layout="wide")

# Detect the browser language
browser_language = detect_browser_language()

# Display content based on the detected language
if browser_language.startswith("es"):
    st.write("¡Hola! Bienvenido a nuestra aplicación.")
elif browser_language.startswith("fr"):
    st.write("Bonjour! Bienvenue dans notre application.")
else:
    st.write("Hello! Welcome to our application.")

# Display the detected language for debugging
st.write(f"Detected browser language: {browser_language}")
