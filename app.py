import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="CGPA Awareness Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .hero-section {
        padding: 2rem 1rem;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        color: #6c757d;
        font-size: 0.9rem;
    }
</style>
""", unsafe_with_html=True)

# 1. Hero Title and Short Intro
st.markdown("""
    <div class="hero-section">
        <h1 style='text-align: center;'>🎓 CGPA Awareness Dashboard</h1>
        <p style='text-align: center; font-size: 1.2rem;'>Empowering College Students to Navigate Academic Success</p>
    </div>
""", unsafe_with_html=True)

st.header("What is CGPA?")
st.markdown("""
Cumulative Grade Point Average (CGPA) is a measure of a student's overall academic performance. It is the average of Grade Points obtained in all subjects (excluding additional subjects) throughout the entire course duration. 
Understanding your CGPA is crucial for tracking your progress and achieving long-term academic goals. For a detailed breakdown of how it's derived, you can consult a [CGPA calculation resource](https://cgpahub.com) to understand the underlying formulas and weightage patterns.
""")

# 2. Why CGPA Matters
with st.container():
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚀 Career & Placements")
        st.write("""
        - **Eligibility Filter:** Many top companies have a minimum CGPA cutoff (often 7.0 or 8.0) to even apply for interviews.
        - **First Impression:** A high CGPA indicates discipline, consistency, and a strong grasp of technical fundamentals.
        - **Higher Studies:** Prestigious universities abroad and in India (like IIMs) heavily weigh CGPA during admissions.
        """)
        
    with col2:
        st.subheader("💰 Scholarships & Financial Aid")
        st.write("""
        - **Merit-Based Grants:** Most corporate and government scholarships require students to maintain a consistent CGPA.
        - **Tuition Fee Waivers:** Many colleges offer fee reductions to the top 5-10% of performers in each department.
        - **Research Opportunities:** High-CGPA students often get preference for funded research internships.
        """)

# 3. Interactive CGPA Simulator
st.divider()
st.header("📊 Interactive CGPA Simulator")
st.info("Simulate your semester-wise performance to see how it affects your overall CGPA.")

num_semesters = st.number_input("How many semesters have you completed?", min_value=1, max_value=8, value=4)

sem_data = []
cols = st.columns(min(4, num_semesters))

for i in range(num_semesters):
    with cols[i % 4]:
        sgpa = st.number_input(f"Sem {i+1} SGPA", min_value=0.0, max_value=10.0, value=7.5, step=0.1, key=f"sem_{i}")
        sem_data.append(sgpa)

# Calculate Average
final_cgpa = sum(sem_data) / len(sem_data)

# 4. Simple Visual Feedback
st.subheader("Current Simulation Result")
col_res, col_msg = st.columns([1, 2])

with col_res:
    st.metric(label="Estimated CGPA", value=f"{final_cgpa:.2f}")
    
with col_msg:
    if final_cgpa >= 9.0:
        st.success("🌟 Outstanding! You are in the top tier. Keep up the consistency.")
    elif final_cgpa >= 8.0:
        st.success("✅ Excellent! Most top companies and universities are within your reach.")
    elif final_cgpa >= 7.0:
        st.warning("📈 Good performance. Improving by 0.5 can significantly open more doors.")
    else:
        st.error("💡 Focus required. Try to aim for 7.5+ in upcoming semesters for better placement opportunities.")

# 5. Educational Tips for Improving CGPA
st.divider()
st.header("💡 Pro Tips for a Higher CGPA")
tip_col1, tip_col2 = st.columns(2)

with tip_col1:
    st.markdown("""
    - **Prioritize High-Credit Courses:** Focus more on subjects with 4+ credits as they impact your CGPA the most.
    - **Attendance is Key:** Beyond the rule, being in class helps you understand the professor's expectations for exams.
    - **Smart Note-Taking:** Quality notes are better than long books for quick revisions.
    """)

with tip_col2:
    st.markdown("""
    - **Master Laboratory Work:** Lab marks are often easier to score high in; don't take them lightly.
    - **Past Year Papers:** Solving previous years' exams gives you a clear pattern of frequently asked questions.
    - **Peer Learning:** Explaining concepts to friends is the best way to solidify your own understanding.
    """)

# 6. Footer
st.divider()
st.markdown("""
    <div class="footer">
        <p><b>Academic Disclaimer:</b> This dashboard is for simulation purposes only. Official CGPA is determined by your University's Examination Cell based on specific credit calculations.</p>
        <p>© 2025 CGPA Awareness Initiative | Empowering Students Digitally</p>
    </div>
""", unsafe_with_html=True)
