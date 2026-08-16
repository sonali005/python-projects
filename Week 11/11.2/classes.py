class Student:

    True

def print_student(student):
    print("Student details: ", student.name, student.id, student.gpa, student.credits)

def main():
    student1 = Student()
    student1.name = "Sonali"
    student1.id = 123
    student1.gpa = 3.8
    student1.credits = 15

    print_student(student1)

    student2 = Student()
    student2.name = "Nada"
    student2.id = 124
    student2.gpa = 4.0
    student2.credits = 18

    print_student(student2)

main()