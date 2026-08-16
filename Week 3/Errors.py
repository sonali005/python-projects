import math

TAX= 0.05

def potentialValueError(x, y):
    
    print(x % y)
    
    
def NameErrorFunc(a,b):
    # No such function "calculateFactorial" is defined here
    # We are calling a function that does not exists
    calculateFactorial(a)
    calculateFactorial(b)
    factorialSum= a+ b
    return factorialSum

def calculateTax(amount):
    finalCalculatedTax= TAX * amount
    return amount  # instead of returning finalCalculatedTax,
                   # we are returning amount which is logically wrong
    

def main():
    #Error 1: potential Value Error (a type of Runtime Error)
    x = int(input("enter x value as integer: "))
    #x=x+1
    y = int(input("enter y value as integer: "))
    #y=y**2
    potentialValueError(x,y) #incase user input string for 'y'

    #Error 2: NameError (a type of Runtime Error)
    NameErrorFunc(5,4)
    
    #Error 3: Attribute Error (a type of Runtime Error)
    #math library does not have pie function/attribute
    piCalc= math.pie * 2
    print(piCalc)
    
    #Semantic Error
    print(calculateTax(500))
    
    
#Syntax error below
# it shoud be == below

if__name__="__main__":   
    main()
    
