def variable_practise():
    monthAge = 223
    noOfDays = 365
    petName = "Snoopy"
    piDigits = 12345
    print(monthAge, noOfDays, petName, piDigits)
variable_practise()


def expressions_practise():
    literal = ("Good morning") #str
    addition = 5+2 #int
    Exponent = 2**3 #power
    Floor = (5/4) #float
    Mod = (11/2) #remainder
    parantheses = (10+5-1) * 8
    operators = ((5+4) - 3) * 2/3
    print(literal, addition, Exponent, Floor, Mod, parantheses, operators)
expressions_practise()


def prompt_and_print():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    add = int(num1 + num2)
    subtract = int(num1 - num2)
    multiply = int(num1) * int(num2)
    divide = float(num1)/float(num2)
    print(add)
    print(subtract)
    print(multiply)
    print(divide)
prompt_and_print()


def main():
    print("Hello python, these are my codes for today: ")
    variable_practise()
    expressions_practise()
    prompt_and_print()
main()
