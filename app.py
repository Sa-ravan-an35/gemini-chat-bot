"""import streamlit as st
import google.generativeai as genai

st.title("Welcome to my Chat Bot")

genai.configure(api_key="AIzaSyBRlkIjZK-XGwJuORMQRhzTkY_O0wJwNMY")

text = st.text_input("Enter your Question ")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message(text)
st.write(response.text)"""

import streamlit as st
import google.generativeai as genai

st.title("Welcome to my Chat Bot")

genai.configure(api_key="AIzaSyBRlkIjZK-XGwJuORMQRhzTkY_O0wJwNMY")

text = st.text_input("Enter your Question ")


if st.button("Click Me!"):
   
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

   
    response = chat.send_message(text)

    
    st.write(response.text)
else:
    st.write("Please enter a question to get a response.")