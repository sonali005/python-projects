"""This python set demonstrates the python sets
as Hashing Data structure"""

def sets_hash(setA):
    print("Printing the received set: ", setA)

    # demonstrating the hashing and watch out the hash values
    for item in setA:
        print(item, "has hash value: ", hash(item))

        # demonstrating how the hash values be used to find indexes (indices)
        array_size = 10
        for item in setA:
            index = hash(item) % array_size
            print(item, "is having index: ", index)



# we want to have a basic set
def main():
    setA = {'apple', 'kiwi', 'cherry', 'date'}
    sets_hash(setA)
if __name__ == "__main__":
    main()

"""From the above demonstrationg we have observed:
Kiwi and date are on index 6 which shows hashing collision
There are 2 techniques to solve the collision:

1 - Open addressing: Where the python algorithm searches for the next available vacant slot in the array

2 - Chaining: Where each index in the array points to a linked list
that holds multiple items mapped to that index

In conclusuion: In python sets and dictionaries, when a hash collision occurs, it doesnt mean that only one value can occupy
the index, rather chaining or other mechanisms will be usedto resolve it"""