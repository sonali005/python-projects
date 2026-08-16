'''This python code will use an arrays.py class'''
import arrays

array_a = arrays.Array(10)   #creating an array of size 10

print(array_a)        #print the array elements
print(array_a[3])     #print the element at index 3 of array_a

length = len(array_a)    #calculates the length of the array which will be 10

for index in range(length):  #running a loop from 0 to length of array
    array_a[index] = index * 5
    print(array_a[index])

array_b = arrays.Array(5, "abc")
print(array_b)
