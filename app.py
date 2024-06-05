import streamlit as st

# Title of the roadmap
st.title("Learning Roadmap")

# Stage 1
st.header("Stage 1: Introduction to Programming")
st.write("""
- Learn the basics of programming
- Recommended Course: [Python for Everybody](https://www.coursera.org/specializations/python)
""")
if st.button('Go to Coursera - Stage 1'):
    st.markdown("[Click here to visit the course](https://www.coursera.org/specializations/python)")

# Stage 2
st.header("Stage 2: Data Structures and Algorithms")
st.write("""
- Understand fundamental data structures
- Learn algorithms and their applications
- Recommended Course: [Algorithms Specialization](https://www.coursera.org/specializations/algorithms)
""")
if st.button('Go to Coursera - Stage 2'):
    st.markdown("[Click here to visit the course](https://www.coursera.org/specializations/algorithms)")

# Stage 3
st.header("Stage 3: Web Development")
st.write("""
- Learn how to build web applications
- Recommended Course: [Full-Stack Web Development](https://www.coursera.org/specializations/full-stack-react)
""")
if st.button('Go to Coursera - Stage 3'):
    st.markdown("[Click here to visit the course](https://www.coursera.org/specializations/full-stack-react)")

# Stage 4
st.header("Stage 4: Data Science and Machine Learning")
st.write("""
- Explore data science techniques
- Learn machine learning algorithms
- Recommended Course: [Machine Learning](https://www.coursera.org/learn/machine-learning)
""")
if st.button('Go to Coursera - Stage 4'):
    st.markdown("[Click here to visit the course](https://www.coursera.org/learn/machine-learning)")

# Add more stages as needed...
