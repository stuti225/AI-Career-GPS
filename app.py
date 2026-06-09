import streamlit as st
import pdfplumber

from skills import SKILLS
from career import recommend_career
from roadmap import get_missing_skills

st.title("AI Career GPS")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

if uploaded_file:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    st.subheader("Detected Skills")
    st.write(found_skills)

    career = recommend_career(found_skills)

    st.subheader("Recommended Career")
    st.success(career)

    missing = get_missing_skills(
        career,
        found_skills
    )

    st.subheader("Missing Skills")
    st.write(missing)

    score = (
        (len(found_skills)) /
        (len(found_skills)+len(missing))
    ) * 100

    st.subheader("Job Readiness Score")

    st.progress(int(score))

    st.write(
        f"{round(score,2)} %"
    )