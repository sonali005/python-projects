# sets in python 

"""setA = {1,2,2,3,4,5,6}
print(setA)

setA.add(6)
setA.add(10)
print(setA)

if 0 in setA:
    print("0 is found in setA")
else:
    print("0 is not found")



# we are now using built in set function
#b_set = set("hello")

b_set = set([777, 123, 876, 233])

listA = sorted(b_set)
print(listA)"""

# subset, superset, union, intersection

def sets_operations():
    setA = {1,2,3,4,5}
    setB = {4,5,6,7,8,}
    setB = {1,2,3,4,5,6,7,8}

    # union of sets
    union = setA.union()
    print("Union of setA and setB: ", union)

    # intersection of sets
    intersection = setA.intersection(setB)
    print("intersection of setA and setB: ", intersection)

    is_subset = setA.issubset(setB)
    print("Is setA a subset of setB: ", is_subset)
    # output will be boolean

    is_superset=setA.issuperset(setB)
    print("Is setA a superset of setB: ", is_superset)

    