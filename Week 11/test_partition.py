def partition(pivot, A):
    less, same, more = [], [], []
    for sort in A:
        if sort < pivot:
            less.append(sort)
        elif sort == pivot:
            same.append(sort)
        else:
            more.append(sort)
    return less, same, more

def test_partition():
    test_array = [3,5,2,8,5]
    pivot = 5
    expected_less = [3,2]
    expected_same = [5,5]
    expected_more = [8]

    less, same, more = partition(pivot, test_array)