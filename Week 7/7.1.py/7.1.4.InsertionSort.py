"""Create a new Python module in a file named “sorts.py” and create a function named “swap” the declares
a parameter for an_array and two indexes named a and b.
Use a temporary variable to swap the values at the indexes.
Add a main function to test your swap function.
Create an array with the values 1-10.
Print the array before and after swapping the values at several indexes.
"""

def swap(an_array, a, b):
    an_array[a], an_array[b] = an_array[b], an_array[a]

def main():
    array = list(range(1, 11))
    print("Before swaps:", array)
    
    swap(array, 0, 9)
    print("After swapping index 0 and 9:", array)
    
    swap(array, 3, 7)
    print("After swapping index 3 and 7:", array)
    
    swap(array, 1, 8)
    print("After swapping index 1 and 8:", array)

if __name__ == "__main__":
    main()
