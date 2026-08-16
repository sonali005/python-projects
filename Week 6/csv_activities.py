import csv

def calculate_class_average(filename, column):
    total = 0  #initialised the total sum of grades
    count = 0  #initialised the count of valid grades

    #opened the csv file
    with open(filename, 'r') as file:
        next(file)


    for line in csv_reader:
        row = line #commas
    grade = float(row[column])
    total = total + grade
    count = count + 1

#calculate the average
    if count > 0:
        average = total / count
        print("Average is", average)
    else:
        print("No grades exist")

calculate_class_average('names.csv', int(3))
