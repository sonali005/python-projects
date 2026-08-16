class student:
    def __init__(self,id="no id",name="no name",credits=0,gpa=0.0):
        self.id=id
        self.name=name
        self.credits=0
        self.gpa=0.0

    def set_details(self,id,name):
        self.id=id
        self.name=name

def main():
        student1=student()
        print(f"id:{student1.id}, name:{student1.name}, credits:{student1.credits}, gpa:{student1.gpa}")
        student1.set_details(12345,"alice") 
        print(f"id:{student1.id}, name:{student1.name}, credits:{student1.credits}, gpa:{student1.gpa}")

        student2=student()
        student2.set_details(4567,"abhi") 
        print(f"id:{student2.id}, name:{student2.name}, credits:{student2.credits}, gpa:{student2.gpa}") 

main()   