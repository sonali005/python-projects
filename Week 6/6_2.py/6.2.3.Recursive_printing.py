"""Rewrite your function that prints odd numbers to use recursion.
● Open your activities module and create a new function called 
“print_odds_rec”. that declares parameters for an_array and 
index=0.
○ The function should perform one unit of work: print a single number.
○ The function should then call itself to handle the remaining work (print the 
remaining numbers).
● In your main function, call the function with the same array used 
previously. What happens?"""

# activities.py

def print_odds_rec(an_array, index=0):
    # Base case: if the index is equal to the length of the array, return
    if index >= len(an_array):
        return
    
    # Print the current value if it is odd
    if an_array[index] % 2 != 0:
        print(an_array[index], end=" ")  # Print odd value with a space
    
    # Recursive call to handle the next index
    print_odds_rec(an_array, index + 1)

def main():
    # Create an array containing values from 0 to 100
    array = list(range(101))  # Values from 0 to 100
    print_odds_rec(array)  # Call the print_odds_rec function

# Run main function if this script is executed directly
if __name__ == "__main__":
    main()
