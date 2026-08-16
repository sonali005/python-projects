

"""class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name  # Assign name to the name object
        self.age = age    # Assign age to the age object

# Creating an instance of the Person class
person1 = Person("Alice", 30)
print("The person's name is", person1.name)  # Output: There person's name is Alice
print("Her age is", person1.age) # Output: Her age is 30"""

class Card:
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = str (rank) + " of " + suit
        self.shorthand = str (rank) + suit[0]

a_card = Card (5, "Hearts")
print(a_card.name)   #output: 5 of Hearts
print(a_card.shorthand)  # Output: 5H







