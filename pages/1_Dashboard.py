import streamlit as st
import pandas as pd
st.title("📋 Dashboard")
if "students" not in st.session_state:
    st.session_state.students = []
if len(st.session_state.students) == 0:
    st.info("No students added yet.")
else:
    df = pd.DataFrame(st.session_state.students)
    st.metric("Total Records", len(df))
    col1,col2,col3=st.columns(3)
    with col1:
        search = st.text_input("🔍 Search Student")
    if search:
        df = df[
            df["Name"].str.contains(
                search,
                case=False
            )
        ]
    with col2:
        subjects = ["All"] + sorted(df["Subject"].unique())
        selected_subject = st.selectbox(
            "📚 Subject",
            subjects
        )
    if selected_subject != "All":
        df = df[
            df["Subject"] == selected_subject
            ]
    with col3:
        sort = st.selectbox(
            "Sort Marks",
            ["Highest First","Lowest First"]
        )
    ascending = sort == "Lowest First"
    df = df.sort_values(
        by="Marks",
        ascending=ascending
    )
    with st.container():
    # Here using enumerate we will get index which will be stored in i
        for i, student in enumerate(st.session_state.students):
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 1])
            with col1:
                st.write(student["Name"])
            with col2:
                st.write(student["Subject"])
            with col3:
                st.write(student["Marks"])
            with col4:
                st.write(student["Age"])
            with col5:
                if st.button("🗑", key=f"delete_{i}"):
                    st.session_state.students.pop(i)
                    st.rerun()
