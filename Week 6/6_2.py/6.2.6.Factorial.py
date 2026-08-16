"""Open your activities module and add a new function named 
“factorial” that declares a parameter for N.
○ Use recursion to implement factorial.
○ Translate the mathematical function (shown to the left) directly into 
Python code.
● Call your new function from main with at least the following values:
○ 10! = 3628800
○ 100! = 9332621544394415268169923885626670049071596826438...
○ 2000! = 331627509245063324117539338057632403828111720810...
"""

def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
    
def main():
    test_values = [10,100]
    for value in test_values:
        result = factorial(value)
        print("Factorial is ", result)
main()