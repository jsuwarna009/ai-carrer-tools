import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# 1. Load the API Key from your .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Resume Polisher", page_icon="🤖")

st.title("🤖 AI Resume Polisher")
with st.sidebar:
    st.title("👨‍💻 Project Info")
    st.markdown("Developed by **Your Name**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/jahnavi-suwarna/)")
    st.markdown("[GitHub](https://github.com/jsuwarna009)")
    st.divider()
    st.info("Built with Llama 3.1 & Streamlit")
st.markdown("Bridge your career gap by highlighting your impact.")

# 2. User Input Fields
job_title = st.text_input("Target Job Title", placeholder="e.g., Senior Software Engineer")
bullet_point = st.text_area("Paste a resume bullet point:", placeholder="e.g., I worked on a health insurance app.")

# 3. The Logic
if st.button("Enhance with AI"):
    if bullet_point and job_title:
        with st.spinner("AI is polishing your achievement..."):
            try:
                # This is the "Prompt" - how we talk to the AI
                prompt = f"You are an expert career coach. Rewrite the following resume bullet point for a {job_title} role. Use strong action verbs and focus on quantifiable impact. Keep it to one powerful sentence: {bullet_point}"
                
                # Sending the request to the Llama 3 model
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}]
                )
                
                # Display the result
                st.success("### Suggested Revision:")
                st.write(completion.choices[0].message.content)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both a job title and a bullet point.")