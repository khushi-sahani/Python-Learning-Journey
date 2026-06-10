import matplotlib.pyplot as plt

students = ["Khushi", "Aman", "Priya"]
marks = [95, 88, 91]

plt.bar(students, marks)

plt.title("Student Marks")

plt.savefig("marks_chart.png")

plt.show()