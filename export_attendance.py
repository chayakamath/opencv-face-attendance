import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('attendance.db')

# Read entire attendance table into pandas dataframe
df = pd.read_sql_query("SELECT * FROM attendance", conn)

# Print attendance
print(df)

# Optional: Export to CSV file
df.to_csv("attendance_report.csv", index=False)
print("Exported to attendance_report.csv")

conn.close()
