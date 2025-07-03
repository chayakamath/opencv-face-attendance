import streamlit as st
import pandas as pd
import sqlite3

st.title("Face Attendance Dashboard")

# Connect to database
conn = sqlite3.connect('attendance.db')
df = pd.read_sql_query("SELECT * FROM attendance", conn)

st.subheader("Today's Attendance")
st.dataframe(df)

if st.button("Export to CSV"):
    df.to_csv("attendance_report.csv", index=False)
    st.success("Exported to attendance_report.csv")

conn.close()
