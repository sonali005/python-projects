"""linear search"""

import arrays as a #using arrays file 
import time 

array_a=a.Array(5)
array_a=[10,20,30,40,50]
target_value=30

begin_time=time.perf_counter() #start time before the search operation 

for i in range (len(array_a)):
    if array_a[i]==target_value:
        print("element found at: ", array_a.index(target_value))


end_time=time.perf_counter() #end time before the search operation 

elapsed_time=end_time-begin_time

print(elapsed_time)
