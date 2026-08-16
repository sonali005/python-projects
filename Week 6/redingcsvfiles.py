#This code will read a csv file

import csv

def read_csv(filePath):
    with open(filePath, 'r') as f:
        # special function to read a csv file
        csvFile=csv.reader(f)
        next(csvFile)

# run a loop to read from csvFile contents
        average = 0
        students = 0
        for line in csvFile:
            #add up the logic here
            #you will need some variables to be initialised 
            #add up index 2 in every row
            average = average +int(line[2])
            students = students + 1 
            print(line)

        total = average/students
        print("The average of the class is", total)


def main():
    filePath = "C:\\Users\\sonab\\OneDrive\\Desktop\\Year 1 Sem 1\\Software\\Vs code python\\names.csv"
    read_csv(filePath)
if __name__ == "__main__":
    main()