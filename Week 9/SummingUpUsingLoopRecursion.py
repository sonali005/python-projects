"""This python code will use a number and sum the numbers
from 1 till that number
First using the loop
Then using recursion"""

def summing_with_loop(number):
    total = 0
    for i in range(1, number + 1):
        total = total+i
    return total

def summing_with_Recursion(number):
    print("************", number)
    if number==1:
        return 1
    else:
        result = number + summing_with_Recursion(number - 1)
        print(result)
        return result


def main():
    number = int(input("enter a number: "))
    result1 = summing_with_loop(number)
    result2 = summing_with_Recursion(number)
    print(result1)
    print(result2)
    
main()