def factorial(n):
    result = 1
    while n > 1:
        result =result* n
        n =n- 1
    return result







def main():
    num = int(input("Enter a positive integer: "))
    returnedResult=factorial(num)
    print()
    print(returnedResult)
        
if __name__=="__main__":
    main()
