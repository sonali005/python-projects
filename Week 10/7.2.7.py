def merge_sort(arr):
    return arr

def main():
    result1 = merge_sort([])
    expected1 = []
    print(f"Test case 1: {'Pass ' if result1 == expected1 else 'Fail'}")

    result2 = merge_sort([1])
    expected2 = [1]
    print(f"Test case 2: {'Pass ' if result2 == expected2 else 'Fail'}")

    result3 = merge_sort([3,2,1])
    expected3 = [1,2,3]
    print(f"Test case 3: {'Pass ' if result3 == expected3 else 'Fail'}")

if __name__ == "__main__":
    main()