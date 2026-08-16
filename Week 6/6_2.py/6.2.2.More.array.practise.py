"""Print only the odd values in an array.
● Open your activities module and create a new function called 
“print_odds” that declares a parameter for an_array.
● Inside the function use a loop to iterate over the values in the array. Print 
all of the odd values on a single line.
○ Hint use the end=" " parameter to the print function.
● In your main function call your print_odds function with an array 
containing the values 0-100."""




def print_odds(an_array):

    for value in an_array:
        if value % 2 != 0:
            print(value, end=" ")


def main():

    array = range(101)
    print_odds(array)
if __name__ == "__main__":
    main()






