import time

def binarySearch(array_a, start, stop, target_value):
    #calculating the midpoint
    mid = (start + stop) // 2
    print("Printing the midpoint", mid)
    
    if start > stop:
        return - 1
    if array_a[mid] < target_value:
        return binarySearch(array_a, mid+1, stop, target_value)
    elif array_a[mid] > target_value:
        return binarySearch(array_a, start, mid-1, target_value)
    elif array_a[mid] == target_value:
        return mid


def main():
    array_a = [20,30,40,60,80,90]
    value = int(input("Enter the value you want to search: "))
    begin = time.perf_counter()
    result = binarySearch(array_a, 0, len(array_a)-1, value)
    end = time.perf_counter()
    total = end - begin
    print(total)
    if result == -1:
        print("Target value not found")
    else:
        print("Target value found")
main()