class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 4.0

def main():
    student1 = Student("12345", "Alice")
    student2 = Student(56789, "Bob")

    print(f"Student 1: ID =  {student1.id}, Name = {student1.name}, Credits = {student1.credits}, GPA ={student1.gpa}")
    print(f"Student 2: ID =  {student2.id}, Name = {student2.name}, Credits = {student2.credits}, GPA ={student2.gpa}")

if __name__ == "__main__":
    main()