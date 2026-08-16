def is_equilateral (a,b,c):
    if a == b and b == c and c == a:
        print("yes") 
    else:
        print("No")
    
def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    result = is_equilateral(a,b,c)
    print(result)
main()