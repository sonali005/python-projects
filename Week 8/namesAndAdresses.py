import csv
path  = "C:\\Users\\sonab\\OneDrive\\Desktop\\name_address.csv"

def read_csv_and_format_printing(path):
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            #Read the recors from the csv file

            for record in reader:
                print("name: <", record[0], "> Address : <", record[1], "> Section: <", record[2], ">")
                print()
    except FileNotFoundError:
        print("file not found, you may not be giving the correct name or path or both")

def main():
    path = "C:\\Users\\sonab\\OneDrive\\Desktop\\name_address.csv"
    read_csv_and_format_printing(path)
if __name__ == "__main__":
    main()