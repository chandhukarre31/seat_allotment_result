
import streamlit as st
import pandas as pd

# Load the result.csv automatically (kept in the same folder as app.py)
@st.cache_data
def load_data():
    return pd.read_csv("result.csv")

df = load_data()

# App title
st.title("🎓 Student Seat Allocation Result Portal")

# Input UniqueID
unique_id = st.text_input("🔑 Enter your UniqueID:")

if unique_id:
    student = df[df['UniqueID'].astype(str) == str(unique_id)]

    if not student.empty:
        st.subheader("📌 Student Allocation Details")
        st.table(student)
    else:
        st.error("❌ No record found for this UniqueID. Please check again.")
