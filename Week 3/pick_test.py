import pick

def test_check_guess_correct():
    assert  pick.check_guess(5,5) == 0

def test_check_guess_to_high(guess, answer):
    assert pick.check_guess(5,3) == "guess it too high"

def test_check_guess_too_low():
    assert pick.check_guess(3,5) == "guess is too low"

def main():
     test_check_guess_correct()
     test_check_guess_to_high()
     test_check_guess_too_low()
     
if __name__ == "__main__":
        main ()