"""This python code will concatenate lists together using + operation"""


def concatenate(a_list, b_list):
    b_list = a_list + b_list
    return b_list



def main():
    a_list = ["a"]
    b_list = ["b"]
    returnedList1 = concatenate(a_list, b_list)
    print(returnedList1)


    first = ["butter"]
    second = "cup"
    returnedList2 = concatenate(first, [second])
    print(returnedList2)

main()