


def factorial(number):
    if number ==1:
        return number
    else:
        return number * factorial(number-1)
    

def main():
    result = factorial(5)
    print(result)
main()
