import streamlit as st
import pandas as pd
st.title("📊 Statistics")
if "students" not in st.session_state:
    st.session_state.students = []
if len(st.session_state.students) == 0:
    st.warning("No student data available.")
else:
    df = pd.DataFrame(st.session_state.students)
    subject_stats = (
        df.groupby("Subject")["Marks"]
        .agg(["mean", "min", "max"])
        .reset_index()
    )
    subject_stats.columns = [
        "Subject",
        "Average Marks",
        "Minimum Marks",
        "Maximum Marks"
    ]
    st.subheader("📚 Subject Statistics")
    st.dataframe(subject_stats, use_container_width=True)
    subjects = df["Subject"].unique()
    for subject in subjects:
        st.subheader(subject)
        subject_df = df[df["Subject"] == subject]
        chart = subject_df.set_index("Name")["Marks"]
        st.bar_chart(chart)
    st.subheader("🏆 Subject Toppers")

    for subject in subjects:
        subject_df = df[df["Subject"] == subject]
        topper = subject_df.loc[
            subject_df["Marks"].idxmax()
        ]
        st.write(
            f"**{subject}** → {topper['Name']} ({topper['Marks']})"
        )