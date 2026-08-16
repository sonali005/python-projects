"""Open your searches module and navigate to your binary_search function.
● Calculate the value of the index at the midpoint.
○ The midpoint should be (start + end) // 2 (floor division)
● If the target value is at the midpoint in the array, we found it!
○ Return the midpoint!
● If the value at the midpoint is less than the target, you should search to the 
right of the midpoint.
○ Set start to 1 more than the midpoint.
○ Make a recursive call to binary_search.
● Otherwise, the target must be to the left of the midpoint (if it is in the array at 
all). 
○ Set end to 1 less than the midpoint.
○ Make a recursive call to binary_search."""

def binary_search(an_array, target, start=None, end=None):
    # Set start and end to the beginning and end of the array if they are None
    if start is None or end is None:
        start = 0
        end = len(an_array) - 1

    # Base case: if start is greater than end, the target is not in the array
    if start > end:
        return None

    # Calculate the midpoint
    mid = (start + end) // 2

    # Check if the middle element is the target
    if an_array[mid] == target:
        return mid
    elif an_array[mid] < target:
        # If target is larger, search in the right half
        return binary_search(an_array, target, mid + 1, end)
    else:
        # If target is smaller, search in the left half
        return binary_search(an_array, target, start, mid - 1)

