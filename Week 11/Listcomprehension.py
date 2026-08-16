
#Recap

# 10 zeros to be printed using list comprehension
ten_zeros = [0 for x in range(10)]       # concise code
print(ten_zeros)       # printing a list with name ten_zeros

# divisible by 3 and 5
divis_3_5 = [i for i in range(50) if i % 3 == 0 and i % 5 == 0]
print(divis_3_5)

# floor division applied on data
data =(20,10,30,8)
listA = [x//2 for x in data]
print(listA)

# table using list comprehension
table = [[row * col for col in range(4)] for row in range(4)]
print(table)
#loop to print it in the form of matrix
for row in table:
    print(row)

# ragged edge 2D list
# calrifying the concept of creating 2d list using loops

table2 = []
for row in range(4):    # for number of rows
    sublist = []
    for col in range(row + 2):   # for num of columns incrementing
        sublist.append(row*col)
    table2.append(sublist)
# print the table using the loop
for r in table2:
    print(RecursionError)





