"""Time linear searches over a very large array.
● Open your activities module and create a new helper function named 
“linear_search_timer” that declares parameters for an_array and a 
target.
○ Return the time it takes to find the target value.
● Create another function named “linear_timer”.
○ Create an array with the values 1 to 10,000,000.
■ Hint: use the range_array function in array_utils.
○ Use your helper function to time how long it takes to find each of the following 
values:
■ first (1)
■ middle (5000000)
■ last (10000000)
● Call your function from main."""

# activities.py
import time

def linear_search(an_array, target):
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None

def linear_search_timer(an_array, target):
    start_time = time.time()  # Record the start time
    linear_search(an_array, target)  # Perform the linear search
    end_time = time.time()  # Record the end time
    return end_time - start_time  # Return the elapsed time

def linear_timer():
    # Create an array with values 1 to 10,000,000
    large_array = list(range(1, 10000001))  # Create a list with numbers from 1 to 10,000,000

    # Values to test: first, middle, last
    targets = [1, 5000000, 10000000]
    for target in targets:
        elapsed_time = linear_search_timer(large_array, target)
        print(f"Time to find {target}: {elapsed_time:.6f} seconds")

def main():
    linear_timer()

if __name__ == "__main__":
    main()
