def fibonacchi(num):
    if num <= 1:
        return num
    else:
        return fibonacchi(num-1) + fibonacchi(num-2)
    
for i in range(10):
        print(fibonacchi(i), end=" ")
