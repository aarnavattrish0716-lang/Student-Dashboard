import streamlit as st
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)
st.title("🏠Student Performance Dashboard")
st.write("""
Welcome to the Student Performance Dashboard!

This application allows you to:
- Add student records
- View all students
- Analyze student performance
- View statistics
""")
st.info("👈 Use the sidebar to navigate between pages")