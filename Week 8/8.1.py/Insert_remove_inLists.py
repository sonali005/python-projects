"""This python code will insert and delete elements from the list using insert and pop functions"""

def remove_with_index(b_list, index):
    removedelement = b_list.pop(index)
    print(removedelement)

def remove_without_index(b_list):
    removedelement = b_list.pop()
    print(removedelement)


def insertion_in_list(a_list):
    a_list.insert(2,3)
    print(a_list)


def main():
    b_list = [2,3,4,5,7]
    print(len(b_list))
    #remove_with_index(b_list, 1)
    #remove_without_index(b_list)
    insertion_in_list(b_list)
    print(len(b_list))
main()