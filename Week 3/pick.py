
def check_guess(guess, answer):
    if guess == answer:
        return 0   
    
    if guess > answer:
        return "guess is too high"
    
    if guess < answer:
        return "guess is too low"

