name = input("Enter Name: ")
marks = input("Enter Marks: ")

file = open("student.txt", "w")

file.write(name + " - " + marks)

file.close()

print("Student Saved Successfully")