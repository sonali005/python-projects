
class Student:
    __slots__ = ['id', 'name', 'grade', 'major']

    def __init__(self, id, name, grade, major):
        self.id = id
        self.name = name
        self.grade = grade
        self.major = major

student = Student(1, "Bayram", "A", "Computer Science")

print(student.name)

try:
    student.name = "Bob"
except AttributeError as e:
    print(f"Error: {e}")

try:
    print(student.name)
except AttributeError as e:
    print(f"Error: {e}")



    