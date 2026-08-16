"""Use a while loop to change the value at every index in an array.

● Add a function to your activities module named “while_fill” that 
declares a parameter for an_array.
● Use a while loop to set the value at each index to match the index.
○ e.g. the value at index 0 is 0, the value at index 1 is 1, and so on.
● Remember, you can use the len() function to get the length of the array!
● In your main function, create an array of size 10 and pass it as an 
argument into the while_fill function.
○ Print the array before and after you call the function!"""

def while_fill(an_array):

    length = len(an_array)
    counter = 0

    while counter < length:
        an_array[counter] = counter
        counter = counter + 1

def main():
    test_array = ["None"] * 10
    print("Array before calling while_fill: ", test_array)

    while_fill(test_array)
    print("Array after calling while_fill: ", test_array)

if __name__ == "__main__":
    main()