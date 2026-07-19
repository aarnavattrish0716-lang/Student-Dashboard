import streamlit as st
## First time Add_Student runs students doesn't exist so Streamlit creates []
# Second time students already exists
if "students" not in st.session_state:
    st.session_state.students=[] # A list will be created
st.title("➕ Add Student")
with st.form("student_form",clear_on_submit=True):
    name = st.text_input("Student Name")
    age = st.number_input(
        "Age",
        min_value=5,
        max_value=30
    )
    subject = st.selectbox(
        "Subject",
        ["Math","Science","English","Computer Science" ]
    )
    marks = st.slider(
        "Marks",
        0,
        100
    )
    submitted = st.form_submit_button("Add Student")
if submitted:
    student={
        "Name":name.strip(),
        "Age":age,
        "Subject":subject,
        "Marks":marks
    }
    updated=False
    for s in st.session_state.students:
        if s["Name"].lower()==name.strip().lower() and s["Subject"]==subject:
            s["Age"]=age
            s["Marks"]=marks
            updated=True
            break
    if updated:
        st.success(f"{name}'s {subject} marks updated!")
    else:
        st.session_state.students.append(student)
        st.success(f"Marks of {name} added successfully!")