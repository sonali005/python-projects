
class Student:
    # Initialize the instance attributes
    def __init__(self):
        self.id = "No ID"
        self.name = "Student"
        self.credits = 0
        self.gpa = 0.0

    # Method to update the attributes
    def set_details(self, id, name):
        self.id = id
        self.name = name

def main():
    # Create student1 and update its details
    student1 = Student()
    student1.set_details("12345", "Alice")

    print(f"ID: {student1.id}, Name: {student1.name}, Credits: {student1.credits}, GPA: {student1.gpa}")

    # Create another student and keep default attributes
    student2 = Student()
    student2.set_details("54321", "Alex")

    print(f"ID: {student2.id}, Name: {student2.name}, Credits: {student2.credits}, GPA: {student2.gpa}")

main()


