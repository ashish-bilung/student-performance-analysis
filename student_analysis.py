import pandas as pd
import matplotlib.pyplot as plt

# Sample student performance data
data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Study_Hours": [2, 5, 3, 8, 6, 4, 7, 1],
    "Attendance": [70, 85, 75, 95, 90, 80, 92, 60],
    "Marks": [45, 68, 52, 88, 76, 61, 82, 35]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Student Performance Dataset:")
print(df)

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Calculate average marks
average_marks = df["Marks"].mean()
print(f"\nAverage Marks: {average_marks:.2f}")

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

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)

plt.savefig("study_hours_vs_marks.png")
plt.show()
