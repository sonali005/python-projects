# searches.py

def linear_search(an_array, target):
    # Loop through the array to search for the target value
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index  # Return the index if the target is found
    return None  # Return None if the target is not found


# Main function to test linear_search
def main():
    # Create an array using a range from 1 to 100
    array = list(range(1, 101))  # Create an array with numbers from 1 to 100

    # Test the linear search with various values
    test_values = [1, 50, 100, 101]
    for value in test_values:
        result = linear_search(array, value)
        if result is not None:
            print(f"Target {value} found at index: {result}")
        else:
            print(f"Target {value} not found in the array.")


# Run main function if this script is executed directly
if __name__ == "__main__":
    main()
