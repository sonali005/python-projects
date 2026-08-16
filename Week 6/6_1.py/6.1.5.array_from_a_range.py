"""Write a utility that will create an array from a range.
● Create a new Python module in a file named “array_utils.py”.
○ Don't forget to import arrays.
● Create a function called “range_array” that declares parameters for start, 
stop, and step=1 (just like a range). 
○ Create a range using the start, stop, and step.
○ Create an array of the same length as the range.
○ Use a loop to copy the range into the array. Remember, you can index into a range, e.g. 
a_range[index]!
○ Return the new array!
● Write a main method to test your new utility function.
○ Call the range_array method with various values for start, stop, and step.
○ Print the arrays that are returned."""

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)

    array_length = len(a_range)
    new_array = [None] * array_length

    for index in range(array_length):
        new_array[index] = a_range[index]

    return new_array

def main():

    print("Array from range(0, 10):", range_array(0, 10))
    print("Array from range(5, 20, 2):", range_array(5, 20, 2))
    print("Array from range(-5, 5):", range_array(-5, 5))
    print("Array from range(10, 0, -2):", range_array(10, 0, -2))

if __name__ == "__main__":
    main()