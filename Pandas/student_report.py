import pandas as pd

df = pd.read_csv("student_data.csv")

print("Total Students =", df["Name"].count())
print("Maximum Marks =", df["Marks"].max())
print("Minimum Marks =", df["Marks"].min())
print("Average Marks =", df["Marks"].mean())
print("Total Marks =", df["Marks"].sum())