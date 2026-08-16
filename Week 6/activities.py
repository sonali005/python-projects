# path = "C:\Users\sonab\OneDrive\Desktop\numbers.txt"

"""Read the file line by line
Cast the numbers into int
add up all the numbers
show the sum at the end"""

import csv

def read_csv(filePath):
    with open(filePath, 'r') as f:
        csvFile = csv.reader(f)
        sum = 0
        for line in f:
            x = line.strip()
            sum = sum + int(x)

        print("The sum is", sum)

def main():
    filePath = "C:\\Users\\sonab\\OneDrive\\Desktop\\numbers.txt"
    read_csv(filePath)
main()