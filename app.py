import streamlit as st
import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")
st.title("📄 AI Resume Analyzer")
st.write("Paste your resume and a job description — get instant AI feedback!")

resume_text = st.text_area("📋 Paste your Resume here", height=250, placeholder="Copy and paste your entire resume text here...")
job_text = st.text_area("💼 Paste the Job Description here", height=200, placeholder="Copy and paste the job description you want to apply for...")

if st.button("🔍 Analyze My Resume"):
    if not resume_text or not job_text:
        st.warning("Please fill in both boxes before analyzing!")
    else:
        with st.spinner("Analyzing your resume... please wait ⏳"):
            prompt = f"""
You are an expert resume coach. Analyze the resume against the job description below.
RESUME: {resume_text}
JOB DESCRIPTION: {job_text}

MATCH SCORE: (score out of 100)
STRENGTHS:
- (3 strengths)
MISSING KEYWORDS:
- (5 missing skills)
TOP 3 TIPS TO IMPROVE:
1. 2. 3.
OVERALL VERDICT: (2 sentences)
"""
            response = model.generate_content(prompt)
            result = response.text

        st.success("✅ Analysis Complete!")
        st.markdown("---")
        st.markdown(result)
        st.download_button(label="📥 Download My Feedback", data=result, file_name="resume_feedback.txt", mime="text/plain")
