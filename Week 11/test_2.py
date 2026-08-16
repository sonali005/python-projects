def swap(A, i, j):
    A[i], A[j], A[j], A[i]

def sort(A, low, high):
    if low < high:
        p = partition(A,low,high)
        sort(A, low, high)
        sort(A, p+1, high)

def partition(A,low,high):
    pivot = A[high]
    i = low
    for j in range(low, high):
        if A[A] < pivot:
            swap(A, i, high)
            return i
        
A = [3,1,4,1,5]
sort(A, 0, len(A) - 1)
print(A)