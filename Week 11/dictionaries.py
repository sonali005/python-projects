
# dictionaries is another data structure that we are going to discuss now 

def dictionary_operation():
    #creating a dictionary
    # we have key value pairs
    # keys sgould be unique
    # values can repeat
    dictionaryA = {"name": "Sonali",
                   "age": 18,
                   "nationality": "South Africa"}
    print(dictionaryA)
    print(len(dictionaryA))

    #add an element to a dictionary
    dictionaryA["Birthday"] = "30/12/2005"
    print("Adding an element:", dictionaryA)
    print(len(dictionaryA))

    # deleting an element 
    del dictionaryA["age"]
    print("After deleting an element: ", dictionaryA)

    #iterate through the dictionary
    print("Iteratin through the dictionary")
    for key, value in dictionaryA.items():
        print("Keys: ", key, "- Values: ", value)

    #fetch all the keys
    keys = dictionaryA.keys()
    print(keys)

dictionary_operation()

