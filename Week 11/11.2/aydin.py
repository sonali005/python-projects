class Student:
 __slots__ = ["id","name","grade","major"]

def _init_(self,id,name,grade,major):
  self.id = id
  self.name = name
  self.grade = grade
  self.major = major
  
  student = Student(1,"Bayram","A","Computer Science")

  print(student.name)+
  
  try:
    student.nname= "Dooper"
  except AttributeError as e:
   print(f"Error: {e}")
  
  try:
   print(student.nname)
  except ArithmeticError as e:
   print(f"Error: {e}")
    