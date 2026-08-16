import random 

# random()
# randint
#randrange

number = random.random()
print(number)

for i in range(10):
    number = random.randint(1,50)
    print(number)

print (random.randrange(3,9))


#activity - roll the dice

def roll_the_die(no_of_sides):
    return random.randint(1, no_of_sides)
    


def main():
    random.seed(1)

    for i in range(10):
        result = roll_the_die(6)
        print(result)
    
main()


# activity 

