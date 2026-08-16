"""Write a function that creates an array filled with random values.
● Open your array_utils module and add a function named 
“random_array” that declares parameters for size, min_value=0, and 
max_value=None.
○ You will need to import the random module.
○ The function should create an array of the specified size.
○ If max_value is None, use size as the max_value.
○ Use a loop to set the value at each index in the array to a pseudorandom number between min_value and max_value.
● Call your new function from main to create an array of size 10 and print 
the array.
● Set the seed used by the pseudo-random number generator to 1 before 
calling the function and rerun your module a few times."""

import random

def random_array(size, min_value=0, max_value=None):
    if max_value is None:
        max_value = size

    new_array = [0] * size

    for index in range(size):
        new_array[index] = random.randint(min_value, max_value - 1)

    return new_array

def main():

    random.seed(1)

    result_array = random_array(10)
    print("Random array of size 10:", result_array)

if __name__ == "__main__":
    main()