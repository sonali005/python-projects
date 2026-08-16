"""In this python program we will execute the rasing error and then 
reraising errors with 2 examples

#raising errors
def guessing_game():
    number = input("Pick a number: ")
    number = int(number)

    # specifying my own game rule, if not followed, should print customised error message
    if number < 1 or number > 10:
        raise ValueError("Invalid guess, please select some number that should be between 1 and 10!")
    print("You picked:", number)

guessing_game()"""


# Reraising error
def validate(userID, passwd):
    correctUID = "rit123"
    correctPwd = "pass123"
    #compare both against the correct ones
    if userID != correctUID or passwd != correctPwd:
        raise ValueError("Invalid User ID or Password or both.  Please try again")


def login():
    attempt = 4 
    while True:
        userID = input("Enter your user ID:")
        passwd= input("Enter your user Password:")
        try:
            validate(userID, passwd)
            print("You are logged in sucessfully")
            break
        except ValueError as ve: 
            attempt = attempt - 1
            if attempt > 0:
                print("Invalid attempt", attempt, "remaining...")
            else:
                print("You are left with no more attempts, Account is locked")
                raise ve
            
def main():
    login()

if __name__ == "__main__":
    main()