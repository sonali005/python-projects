"""This python program will use Python array module
to create and change, and traverse through all the 
elements of array"""


import array

"""array_a = a.array('i', [1,2,4,5])
print(array_a)

for index in range(len(array_a)):
    print(array_a[index])"""


# activity 2 

def while_fill(an_array):
    counter = 0
    
    while counter < len(an_array):
        an_array[counter] = counter 
        counter = counter + 1 


def main():
    x = array.array(10)
    print(x)

    while_fill(x)
    print(x)


main()