"""Write a function that creates a list, prints the elements inside of it, and then returns it
● Open your activities module and add a function named “lists”.
○ Create a list using a list literal with at least 5 values or various types.
○ Use a loop to print each of the elements in the list on a separate line.
○ What happens if you try to change one of the values in the list using its index?
○ Return the list.
● Call your function from main and print the list that it returns.
○ Don’t use a loop, just pass the list into the print() function"""

def lists():
    lista = [2, "abcd", False, 3.14]

    for element in lista:
        print(element)

    lista[0] = 42
    print(lista)

    return lista

def main():
    returnedlists = lists()
    print("the returned list is", returnedlists)
main()