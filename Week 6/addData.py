'''How to add data to a file?'''

import csv

#prompt the suer

name = input("Enter name: ")
age = input("Enter age: ")
grade = input("Enter grade: ")


with open('names.csv', 'a', newline = '') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([name, age, grade])

print("data saved")
