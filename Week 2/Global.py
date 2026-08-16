pi= 3.14

def circle_area(radius):
      return pi * radius ** 2
  
  
def circle_circumference(radius):
      
      return 2 * pi * radius
  
def div(a,b):
    divResult= a/b
    #return a  # semantic error
    return divResult
def main():
    
      radiusVal=int(input("enter the value of radius"))
      area = circle_area(radiusVal)
      print(area)
      circumference= circle_circumference(10)
      print(circumference)
      a=10
      b=2
      print(div(a,b))
      
      
main()
