import streamlit as st
from groq import Groq # Or openai if using OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🤖 AI Resume Polisher")

job_title = st.text_input("Target Job Title")
bullet_point = st.text_area("Paste a resume bullet point:")

if st.button("Enhance with AI"):
    if bullet_point and job_title:
        # The AI Prompt
        prompt = f"Rewrite this resume bullet point for a {job_title} role to sound more impactful and professional: {bullet_point}"
        
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        
        st.success(completion.choices[0].message.content)
    else:
        st.error("Please fill in both fields!")