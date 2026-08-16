'''
Write code to print the expected output using nested loop
Expected Output:
1
22
333
4444
55555
666666
'''
for i in range(1, 7):
    for j in range(i):
        print(i, end="") #note that end="" just combines digits in 1 line
    print()
