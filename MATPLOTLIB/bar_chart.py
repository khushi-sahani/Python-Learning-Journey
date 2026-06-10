import matplotlib.pyplot as plt

students = ["Khushi", "Aman", "Priya"]
marks = [95, 88, 91]

plt.bar(students, marks, color="green")

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()