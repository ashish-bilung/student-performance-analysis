import pandas as pd
import matplotlib.pyplot as plt

# Load student performance dataset
df = pd.read_csv("student_performance.csv")

# Display the dataset
print("Student Performance Dataset:")
print(df)

# Basic statistics
average_marks = df["Marks"].mean()
average_attendance = df["Attendance"].mean()
average_study_hours = df["Study_Hours"].mean()

print(f"\nAverage Marks: {average_marks:.2f}")
print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Average Study Hours: {average_study_hours:.2f}")

# Find the student with the highest marks
top_student = df.loc[df["Marks"].idxmax()]

print("\nTop Performing Student:")
print(top_student)

# Correlation between study hours and marks
correlation = df["Study_Hours"].corr(df["Marks"])

print(f"\nCorrelation between Study Hours and Marks: {correlation:.2f}")

# Create visualization
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Marks"])

plt.title("Study Hours vs Student Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid(True)
plt.savefig("study_hours_vs_marks.png")
plt.show()
