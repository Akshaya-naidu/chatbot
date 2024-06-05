import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        color: #800080; /* Purple */
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    .header {
        color: #FF1493; /* Pink */
        font-size: 30px;
        font-weight: bold;
    }
    .button {
        background-color: #FF69B4; /* Pink */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        display: inline-block;
        font-size: 16px;
    }
    .button:hover {
        background-color: #C71585; /* Darker Pink */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the roadmap
st.markdown('<div class="title">Interactive Learning Roadmap</div>', unsafe_allow_html=True)

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
st.markdown('<div class="header">Stage 1: Introduction to Programming</div>', unsafe_allow_html=True)
selected_course_1 = st.selectbox("Choose a course for Stage 1", list(stage_1_options.keys()))
if st.button(f'Go to {selected_course_1}'):
    st.markdown(f"<a href='{stage_1_options[selected_course_1]}' class='button' target='_blank'>Click here to visit the course</a>", unsafe_allow_html=True)

# Stage 2
st.markdown('<div class="header">Stage 2: Data Structures and Algorithms</div>', unsafe_allow_html=True)
selected_course_2 = st.selectbox("Choose a course for Stage 2", list(stage_2_options.keys()))
if st.button(f'Go to {selected_course_2}'):
    st.markdown(f"<a href='{stage_2_options[selected_course_2]}' class='button' target='_blank'>Click here to visit the course</a>", unsafe_allow_html=True)

# Stage 3
st.markdown('<div class="header">Stage 3: Web Development</div>', unsafe_allow_html=True)
selected_course_3 = st.selectbox("Choose a course for Stage 3", list(stage_3_options.keys()))
if st.button(f'Go to {selected_course_3}'):
    st.markdown(f"<a href='{stage_3_options[selected_course_3]}' class='button' target='_blank'>Click here to visit the course</a>", unsafe_allow_html=True)

# Stage 4
st.markdown('<div class="header">Stage 4: Data Science and Machine Learning</div>', unsafe_allow_html=True)
selected_course_4 = st.selectbox("Choose a course for Stage 4", list(stage_4_options.keys()))
if st.button(f'Go to {selected_course_4}'):
    st.markdown(f"<a href='{stage_4_options[selected_course_4]}' class='button' target='_blank'>Click here to visit the course</a>", unsafe_allow_html=True)
