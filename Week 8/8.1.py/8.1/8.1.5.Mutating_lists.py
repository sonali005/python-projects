""" Open your activities module and add a new function named 
“make_list” that declares a parameter for a_sequence.
○ Create an empty list.
○ Use the append() function to add the values from a_sequence onto 
the list. Print the list each time a value is appended.
○ Return the list.
● In your main function:
○ Call your make_list function with the sequence of your choice (e.g. a 
range, string, etc.).
○ Print the list returned by the function."""

def make_list(a_sequence):
    lista = []

    for element in a_sequence:
        lista.append(element)
        print(lista)

    return lista

def main():
    sequence = range(1,10)
    returned_list = make_list(sequence)
    print("This is the returned list: ", returned_list)
main()