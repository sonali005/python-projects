"""This python codw will sum up large number
in each iteration of loop
and calculate how much time it has taken"""

import time

def summing():
    sum = 0
    for number in range(1000000):
        sum = sum + number


def main():
    
    begin_time = time.perf_counter()
    summing()
    end_time = time.perf_counter()
    elapsed_time = end_time - begin_time
    
    print(elapsed_time)
main()