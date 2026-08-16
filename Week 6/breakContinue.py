"""_summary
Using while true, print the numbers from 1 till 30
skip the numbers which are divisble by 3 
and break the loop for numbers > 30
"""

def num():
    count = 1
    while True:
        count = count + 1 
        if count%3 == 0:
            continue
        elif count >=30:
            break
        else:
            print(count)
        

def main():
    num()
main()
     