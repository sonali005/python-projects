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

def quicksort(A):
    if not A:
        return []
    else:
        pivot = A[0]
        less, same, more = partition(pivot, A)
        return quicksort(less) + same + quicksort(more)

A = [3,4,6,7,2,8,10,4,5]
sorted_A = quicksort(A)
print(sorted_A)

