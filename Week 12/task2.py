def make_table(rows, column, default_value):
    table = []
    for _ in range(rows):
        rows = [default_value] * column 
        table.append(rows)

    for row in table:
        print(row)

    return table 

def main():
    row = int(input("Enter the amount of rows: "))
    column = int(input("Enter the amount of columns you want: "))
    default_value = (input("Enter a default value: "))

    make_table(row,column,default_value)
main()
