import matplotlib.pyplot as plt

students = ["Khushi", "Aman", "Priya", "Riya"]
marks = [95, 88, 91, 85]

plt.bar(students, marks, color="green")

plt.title("Student Marks Report")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.savefig("student_report.png")

plt.show()