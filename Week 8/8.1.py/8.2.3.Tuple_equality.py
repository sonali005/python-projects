"""Create different tuples with the same values and compare them for equality.
● Open your activities module and add a new function named “tuple_equality” 
that declares parameters for two tuples.
○ Print both tuples.
○ Compare the tuples using the is operator and print the results.
○ Compare them again using the == operator and print the results.
● In your main function:
○ Create a list with 3 or more values of varying types in it.
○ Use the built-in tuple() function to create a tuple from the elements in your list, e.g. 
a_tuple = tuple(a_list) and call your tuple_equality using the tuple as an 
argument to both parameters, e.g. tuple_equality(a_tuple, a_tuple)
○ Create a second tuple using the tuple() function with the same list, and call your 
tuple_equality function with both tuples.
○ Create a third tuple with the same values in a different order. Call your function with it 
and one of your other tuples."""

def tuple_equality(a_tuple, b_tuple):

    #check the shallow and deeep equality
    print(f"Using is operator: {a_tuple is b_tuple}")  #shallow equality
    print(f"Using is operator: {a_tuple == b_tuple}")  #deep equality



def main():
    list_a = ['a', 3, 3.0]
    list_b = ['a', 3, 3]


    tupleA = tuple(list_a)
    tupleB = tuple(list_b)

    tuple_equality(tupleA, tupleB)

main()