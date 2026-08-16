#for tab you will use\t
#for separate lines use "\n"
#for enclosed quotes use '....'"
#use \b to delete

Course1 = "GCIS-\b123"
Course2 = "NSSA-\b201"
Course3 = "ISTE-\b102"
path = "C:\\Users\\MAK\\"

print(Course1, "\n", Course2, "\n", Course3)

def mixedquotes():
    print("She said \"I dont like broccoli.\"")
mixedquotes()

def tab():
    print("A\t B\t")
tab()

def backSlashes():
    print("This/ is\\ a/ test\\")
backSlashes()

def newLines():
    print("This\n is a string\n with new lines in\n the middle")
newLines()


stringMessage = "Skywalker"
length = len(stringMessage)
print(length)

print(stringMessage[0])
print(stringMessage[5])
print(stringMessage[8])
print(stringMessage[-1])
print(stringMessage[-5])