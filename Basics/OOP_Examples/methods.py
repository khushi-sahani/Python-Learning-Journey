class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print("Name =", self.name)
        print("Marks =", self.marks)

s1 = Student("Khushi", 95)

s1.show()