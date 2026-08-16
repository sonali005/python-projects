def whileBreak():
    #flag = True
    while True:
        user = input("Enter a character: ")
        if user == "x":
            break
whileBreak()

def whileContinue():
    #flag = True
    while True:
        user = input("Enter a character: ")
        if user == "x":
            continue
        print(user)
whileBreak()