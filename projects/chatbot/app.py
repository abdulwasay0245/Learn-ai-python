import streamlit as st
from google import genai

st.header("Ai featured chatbot")
user_input = st.text_input("Write something to generate: ")

# prompt = input("ENTER YOUR PROMPT:  ")
def generate_text(prompt):
    try:
        client = genai.Client(api_key="AIzaSyCHwCpVOvHQlIUQIB-m-CvOf46MHpO3PbY")
        
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents= prompt,
          )

        st.write(response.text)
    except Exception as e:
        st.write(f"An error occured {e}")

generate_text(user_input)


st.subheader("Developed by Abdul Wasay")