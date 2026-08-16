"""Write a function that uses a tuple.
● Create a new Python module in a file named “activities.py” and add a 
function named “tuples” that declares a parameter for a_tuple. 
○ Print the length of a_tuple.
○ Print a_tuple.
○ Print each of the elements inside of a_tuple on a separate line.
○ What happens if you try to change one of the elements using its index?
● Add a main function and call the function with several different tuples"""

def tuples(a_tuple):
    length = len(a_tuple)
    print("This is the length of a_tuple: ", length)

    print(a_tuple)  #prints the tuple

    for element in a_tuple:   #prints the element in a tuble on a new line
        print(element)
    

def main():
    a_tuple = (1,2,3,4,5)
    tuples(a_tuple)
main()