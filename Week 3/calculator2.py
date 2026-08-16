def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(number1, number2):
    difference = number1 - number2
    return difference

def multiply(number1, number2):
    product = number1 * number2
    return product

def divide(number1, number2):
    result = number1 - number2
    return result

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    x = add(num1, num2)
    print(x)

    y = subtract(num1, num2)
    print(y)

    z = multiply(num1, num2)
    print(z)

    s = divide(num1, num2)
    print(s)
main()



