"""Use a for loop to change the value at every index in an array.
● Add a function to your activities module named “for_fill”.
● Use a for loop to set the value at each index to match the index.
○ e.g. the value at index 0 is 0, the value at index 1 is 1, and so on.
● Remember, you can use the len() function to get the length of the array!
● In your main function, create an array of size 10 and pass it as an 
argument into the for_fill function.
○ Print the array before and after you call the function!
"""

def for_fill(an_array):
    length = len(an_array)

    for index in range(length):
        an_array[index] = index

def main():
    test_array = ["None"] * 10
    print("Array before calling for_fill: ", test_array)

    for_fill(test_array)
    print("Array after calling for fill: ", test_array)

if __name__ == "__main__":
   main()