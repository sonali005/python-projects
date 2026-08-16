"""Write a function that, given a number of sides, generates a 
random die roll. 
● Open your activities module and add a new function named 
roll_the_die that declares a single parameter for the number of sides.
○ You will need to import the random module.
○ The function should return a random number between 1 and the number of sides.
● In your main function, use a loop to call your die rolling function for a 6-
sided die at least 10 times and print the result.
● Run your module a few times"""

import random

def roll_the_die(num_sides):

    return random.randint(1, num_sides)
    

def main():

    random.seed(1)  #rerolling the dice with seed 

    print("Rolling a 6-sided die 10 times:")
    for index in range(10):
        result = roll_the_die(6)
        print(result)

if __name__ == "__main__":
    main()














