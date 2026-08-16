"""Write a function that makes and prints a few arrays.
● Create a new Python module in a file named “activities.py”.
● Add a function named “making_arrays”.
● Inside the function, create and print each of the following arrays. 
○ Size: 5, No prototype
○ Size: 1, Prototype 0
○ Size: 10, Prototype: "" (Empty string)
○ Size: 20, Prototype: False
● Add a main function that calls making_arrays."""


def making_arrays():
    array_1 = [None] * 5 
    print("Array of size 5, prototype is None: ", array_1)

    array_2 = [0] * 1
    print("Array of size 1, prototype is 0: ", array_2)

    array_3 = [""] * 10
    print("Array of size 10, prototype is "": ", array_3)

    array_4 = ["False"] * 20
    print("Array of size 20, prototype is False: ", array_4)

def main():

    making_arrays()

if __name__ == "__main__":
    main()



