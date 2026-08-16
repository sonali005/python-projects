"""Call your countdown function with a number large enough to 
exceed the maximum recursion depth.
13
● Open your activities module and navigate to your main function.
● Call your countdown function with an argument of 100000.
● Boom! """


# activities.py

def countdown(number):
    if number == 0:
        return 0
    else:
        return number + countdown(number - 1)

def main():
    try:
        result = countdown(100000)
        print(f"The sum of numbers from 100000 down to 0 is: {result}")
    except RecursionError:
        print("Boom! Recursion limit exceeded for countdown(100000)!")
main()
