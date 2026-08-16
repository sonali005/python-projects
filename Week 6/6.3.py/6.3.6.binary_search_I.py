"""Open your searches module and create a new function called 
“binary_search” that declares parameters for an_array, a target value, 
start=None, and end=None.
● If start is None, set start and end to the appropriate indexes.
● Implement the base case: if start is greater than end, the value is not in the 
array, so return None."""


def binary_search(an_array, target_value, start=None, end=None):
    if start is None or end is None:
        start = 0
        end = len(an_array-1)

    if start > end:
        return None
    
    mid = (start+end) // 2

    if an_array[mid] == target_value:
        return mid
    elif an_array[mid] > target_value:
        return binary_search(an_array, target_value, start, mid-1)
    else:
        return binary_search(an_array, target_value, mid+1, end)

