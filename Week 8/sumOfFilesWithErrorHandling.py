"""This python program will receive the name of file(s) until the user
types none or blank as fileName.  Then it should read all the numbers from 
the file(s) which user has input, and give the Final sum
We will use Error handling"""

def sum_of_file_numbers():
    total_sum = 0
    while True:
        fileName = input("Enter a file (along with path) or press enter to stop")

        if fileName =="":
            break

        try:
            #read the file 
            with open(fileName, 'r') as file:
                file_sum = 0
                #start reading the lines in the file one by one
                for line in file:
                    try:
                        file_sum = file_sum + int(line.strip())
                    except ValueError:
                        print("Skipping invalid number line")
                print("sum of the numbers: ", file_sum)
                    #This will give the sume of all the sums_of_the_files
                total_sum = total_sum + file_sum

        except FileNotFoundError:
            print("File not found, please enter the correct file name (along with the path)")
    print("Total sum of all the numbers of all the files: ", total_sum)

sum_of_file_numbers()

