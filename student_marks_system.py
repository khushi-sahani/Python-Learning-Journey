students = {
    "Khushi": 95,
    "Aman": 88,
    "Priya": 91
}

name = input("Enter student name: ")

if name in students:
    print("Marks =", students[name])
else:
    print("Student Not Found")