"""Write a recursive function that counts down from some 
number and returns the sum of the numbers printed.
Open your activities module and create a new function named 
“countdown” that declares a parameter for the number.
○ Use recursion to implement the countdown.
○ What is the base case? What work, if any, should it do?
○ What is the recursive case?
○ Return the sum of all of the numbers.
● Call your new function from main and print the sum.
"""

def countdown(num):
    if num == 0:
        return 0
    else:
        return num + countdown(num-1)
    
def main():
    num = 5
    total_sum = countdown(num)
    print("The total sum is ", total_sum)
main()

