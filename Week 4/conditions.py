def conditions_check():
    num1 = int(input("Enter a value: "))
    num2 = int(input("Enter another a value: "))
    if num1 == num2:
        print("num1 is equal to num2")
    elif num1<num2:
        print("num1 is less than num2")
    elif num1>num2:
        print("num1 is greater than num2")
    else:
        print("both num1 and num2 are undefined")


def evenNumbers():
    number = int(input("Enter a number to check whether it is even or odd "))
    if number % 2 == 0:
        print("The", number,"is even")
    else:
        print("The ", number, "is odd")


def divisible():
    for x in range(1,11):
        if x % 3 == 0:
            print(x, "is divisible by 3")
        else:
            print(x, "is not divisble by 3")


def grades():
    mark = int(input("Enter the students score: "))
    if mark == 100:
        print("This student received an A")
    if (100>mark<=90): 
        print("This student has received a B")
    
    

def main():
    #conditions_check()
    #evenNumbers()
    #divisible()
    grades()
main()