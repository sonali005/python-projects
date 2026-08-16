"""Create a new Python module in a file named “activities.py” and create a function named “evens” 
that, declares a parameter for an integer n.
Compute and return the sum of the even numbers from 0 to n.
Create another new function named “runner” that declares parameters for another function and a number.
Print the __name__ of the function before you call it.
Call the function parameter with the number.
Print the value that is returned by the function.
Call runner from main with your evens function and the number of your choice.
"""

# activities.py

def evens(n):
    # Calculate the sum of even numbers from 0 to n
    return sum(i for i in range(0, n+1, 2))

def runner(function, number):
    # Print the name of the function
    print("Function name:", function.__name__)
    # Call the function with the number and print the result
    result = function(number)
    print("Result:", result)

def main():
    # Call runner with evens function and a chosen number, e.g., 10
    runner(evens, 10)

# Call main to run the program
if __name__ == "__main__":
    main()
