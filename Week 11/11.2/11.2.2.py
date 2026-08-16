class Student:
    # Default class attributes
    id = "No ID"
    name = "Student"
    credits = 0
    gpa = 0.0

    # Method to initialize the attributes
    def set_details(self, id, name):
        Student.id = id
        Student.name = name

def main():
    # Create student1 and update its details
    student1 = Student()
    student1.set_details("12345", "Alice")

    # Display student1's details
    print(f"ID: {student1.id}, Name: {student1.name}, Credits: {student1.credits}, GPA: {student1.gpa}")

    # Create another student and keep default attributes
    student2 = Student()
    student1.set_details("54321", "alex")
    print(f"ID: {student2.id}, Name: {student2.name}, Credits: {student2.credits}, GPA: {student2.gpa}")

main()




