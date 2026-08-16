"""Calling a function from within another function
Expected Output:
    hello
    
    hello
    GCIS
    hello
    
    hello
    GCIS
    hello
    
    hello
"""

def hello():
    print("Hello")
    
def gcis():
    hello()
    print("gcis")
    hello()
    
def main():
    hello()
    print()
    gcis()
    print()
    gcis()
    print()
    hello()
if __name__=="__main__":
    main()
    