import streamlit as st
import google.generativeai as genai
import os

key = os.getenv("GEMINI_API_KEY")

# API key
genai.configure(api_key= key)

# Configure Model
model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp", 
                              system_instruction="""Analyze the submitted code and identify potential bugs,
                              errors, or areas of improvement.Generate Bug Report and Fixed Code only.""")


# streamlit
st.title("An AI Code Reviewer 🤖")

user_prompt = st.text_area("Enter Your Python Code here...", height = 200)

if st.button("submit the code"):
    st.subheader("Code Review")
    response = model.generate_content(user_prompt)
    st.write(response.text)
    

