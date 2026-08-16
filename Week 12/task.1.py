def comprehension():
    letters = [char for char in "foobar"]
    print("letters in 'foobar': ", letters)

    zero = [0 for i in range(15)]
    print("15 zeros: ", zero)

    integers_0_to_20 = [i for i in range(20)]
    print("integers from 0 to 20: ", integers_0_to_20)

    even_integers = [i for i in range(21) if i % 2 == 0]
    print("Even integers between 0 and 20: ", even_integers)

    divisble_by_3_or_5 = [i for i in range(50) if i % 3 == 0 or i % 5 == 0]
    print("Integers less than 50 divisible by 3 or 5: ", divisble_by_3_or_5)

    divisible_by_3_not2 = [i for i in range(50) if i % 3 == 0 and 1 % 2!= 0]
    print("integers less than 50 divisble by 3: ", divisible_by_3_not2)

    divisble_by_5 = [i for i in range(0,25) if i % 5 == 0 and str(i)[-1]=="5"]
    print("Integers less than 25 divisible by 5: ", divisble_by_5)

comprehension()