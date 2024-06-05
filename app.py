import streamlit as st

# Title of the roadmap
st.title("Interactive Learning Roadmap")

# Define options for each stage
stage_1_options = {
    "Python for Everybody": "https://www.coursera.org/specializations/python",
    "Introduction to Computer Science": "https://www.coursera.org/learn/cs50",
    "Programming for Everybody (Getting Started with Python)": "https://www.coursera.org/learn/python"
}

stage_2_options = {
    "Algorithms Specialization": "https://www.coursera.org/specializations/algorithms",
    "Data Structures and Algorithms": "https://www.coursera.org/specializations/data-structures-algorithms",
    "Algorithmic Toolbox": "https://www.coursera.org/learn/algorithmic-toolbox"
}

stage_3_options = {
    "Full-Stack Web Development": "https://www.coursera.org/specializations/full-stack-react",
    "Web Design for Everybody": "https://www.coursera.org/specializations/web-design",
    "Responsive Website Development and Design": "https://www.coursera.org/specializations/website-development"
}

stage_4_options = {
    "Machine Learning": "https://www.coursera.org/learn/machine-learning",
    "Applied Data Science with Python": "https://www.coursera.org/specializations/data-science-python",
    "Deep Learning Specialization": "https://www.coursera.org/specializations/deep-learning"
}

# Stage 1
st.header("Stage 1: Introduction to Programming")
selected_course_1 = st.selectbox("Choose a course for Stage 1", list(stage_1_options.keys()))
if st.button(f'Go to {selected_course_1}'):
    st.markdown(f"[Click here to visit the course]({stage_1_options[selected_course_1]})")

# Stage 2
st.header("Stage 2: Data Structures and Algorithms")
selected_course_2 = st.selectbox("Choose a course for Stage 2", list(stage_2_options.keys()))
if st.button(f'Go to {selected_course_2}'):
    st.markdown(f"[Click here to visit the course]({stage_2_options[selected_course_2]})")

# Stage 3
st.header("Stage 3: Web Development")
selected_course_3 = st.selectbox("Choose a course for Stage 3", list(stage_3_options.keys()))
if st.button(f'Go to {selected_course_3}'):
    st.markdown(f"[Click here to visit the course]({stage_3_options[selected_course_3]})")

# Stage 4
st.header("Stage 4: Data Science and Machine Learning")
selected_course_4 = st.selectbox("Choose a course for Stage 4", list(stage_4_options.keys()))
if st.button(f'Go to {selected_course_4}'):
    st.markdown(f"[Click here to visit the course]({stage_4_options[selected_course_4]})")

# Add more stages as needed...
