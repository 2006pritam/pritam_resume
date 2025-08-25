import streamlit as st
from datetime import date
import requests

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Pritam Kumar Modak - Resume", layout="wide")

# ---------------- SIDEBAR PROFILE ----------------
with st.sidebar:
    st.image("https://github.com/2006pritam/PHOTO/raw/main/Screenshot%202025-08-13%20204335.png", width=150)
    st.markdown("### Pritam Kumar Modak")
    st.caption("🎓 BCA Student | Future Software Developer")

    st.write("📞 +91 9064662830")
    st.write("✉️ [modakpritam06@gmail.com](mailto:modakpritam06@gmail.com)")
    st.write("🔗 [LinkedIn](https://in.linkedin.com/in/pritam-modak-267164288)")
    st.write("🐙 [GitHub](https://github.com/2006pritam)")

    st.markdown("---")
    st.title("📑 Navigation")
    page = st.radio("Go to", [
        "Personal Details", 
        "Career Objective", 
        "Education", 
        "Technical Skills", 
        "Projects", 
        "Certifications", 
        "Internship", 
        "Extracurriculars",
        "Contact"
    ])

# ---------------- AGE CALC ----------------
birthdate = date(2006, 1, 19)
today = date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# ---------------- MAIN CONTENT ----------------
st.title("Resume - Pritam Kumar Modak")

if page == "Personal Details":
    st.subheader("Personal Details")
    st.table({
        "Field": ["Name", "Father's Name", "Mother's Name", "Address", "Age"],
        "Details": [
            "Pritam Kumar Modak",
            "Uttam Kumar Modak",
            "Sutapa Modak",
            "Puratan hat, Nibhuji Bazar, Kalna, Purba Bardhaman, West Bengal, India, 713434",
            str(age)
        ]
    })

elif page == "Career Objective":
    st.subheader("Career Objective")
    st.write("""
    Pritam Kumar Modak | Computer Applications Student | Hailing from Kalna, West Bengal.  
    I am pursuing my Bachelor’s degree at Supreme Institute of Management and Technology, with aspirations of becoming a software developer at Google.  
    Committed to learning and growth in the tech field. ☎ #TechCareer #SoftwareDeveloper #DreamBig
    """)

elif page == "Education":
    st.subheader("Education")
    st.markdown("""
    <table>
    <tr><th>Degree / Class</th><th>Institution</th><th>Board / University</th><th>Year</th><th>Result</th></tr>
    <tr><td>BCA</td><td>Supreme Institute of Management and Technology</td><td>MAKAUT</td><td>2026 (Expected)</td>
    <td>SGPA:<br>1st sem :- 8.45<br>2nd sem :- 8.24<br>3rd sem :- 7.24<br>4th sem :- 7.05</td></tr>
    <tr><td>Higher Secondary (12th)</td><td>Maharaja’s High School, Kalna</td><td>WBCHSE</td><td>2023</td><td>73.2%</td></tr>
    <tr><td>Secondary (10th)</td><td>Maharaja’s High School, Kalna</td><td>WBBSE</td><td>2021</td><td>75%</td></tr>
    </table>
    """, unsafe_allow_html=True)

elif page == "Technical Skills":
    st.subheader("Technical Skills")
    st.markdown("""
    <div style="margin:8px 0;">
    <span style="background:#007bff;color:white;padding:5px 10px;border-radius:20px;margin:3px;">Python</span>
    <span style="background:#007bff;color:white;padding:5px 10px;border-radius:20px;margin:3px;">C / C++</span>
    <span style="background:#007bff;color:white;padding:5px 10px;border-radius:20px;margin:3px;">HTML / CSS / JS</span>
    <span style="background:#007bff;color:white;padding:5px 10px;border-radius:20px;margin:3px;">React.js</span>
    <span style="background:#007bff;color:white;padding:5px 10px;border-radius:20px;margin:3px;">MySQL</span>
    <span style="background:#007bff;color:white;padding:5px 10px;border-radius:20px;margin:3px;">Git / GitHub</span>
    <span style="background:#007bff;color:white;padding:5px 10px;border-radius:20px;margin:3px;">DSA</span>
    </div>
    """, unsafe_allow_html=True)

elif page == "Projects":
    st.subheader("Projects")
    st.write("""
    - Front Page Builder (React, TypeScript)  
    - Password Generator (React)  
    - Weather System (API, React)  
    - Personal Portfolio (React)  
    """)

elif page == "Certifications":
    st.subheader("Certifications")
    st.write("""
    - Python for Data Science – IBM (2025)  
    - Advanced JavaScript – HackerRank (2024)  
    """)

elif page == "Internship":
    st.subheader("Internship")
    st.write("University of Calcutta – AIML Research (Jun 2025 – Present)")

elif page == "Extracurriculars":
    st.subheader("Extracurriculars")
    st.write("Basic Computer Skills – Brainpower Computer Academy (2013–2019)")

elif page == "Contact":
    st.subheader("📩 Contact & Feedback")

    # --- Download CV Button ---
    cv_url = "https://drive.google.com/uc?export=download&id=19bKHBNM7iinGYrsNWNPPpDq2K73TR91c"
    st.markdown(
        f'<a href="{cv_url}" target="_blank">'
        '<button style="background:#007bff;color:white;padding:10px 20px;'
        'border:none;border-radius:8px;cursor:pointer;font-size:16px;">📄 Download CV</button></a>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    # --- Feedback Form ---
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Feedback")

        submitted = st.form_submit_button("Submit Feedback")

        if submitted:
            if name and email and message:
                try:
                    response = requests.post(
                        "https://formspree.io/f/mwpqgjvv",
                        data={"name": name, "email": email, "message": message}
                    )
                    if response.status_code == 200:
                        st.success("✅ Thank you! Your feedback has been submitted successfully.")
                    else:
                        st.error("❌ Something went wrong. Please try again later.")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
            else:
                st.warning("⚠️ Please fill out all fields before submitting.")
