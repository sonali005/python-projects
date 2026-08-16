def mutater(a_list, an_int):
    print("an_int:", an_int)
    print("a_list:", a_list)

    an_int *= 5 
    a_list[0] *= 5 

    
    print("new values")
    print("an_int:", an_int)
    print("a_list:", a_list)

def main():
    an_int = 10 
    a_list = [an_int] 
    mutater(a_list, an_int)

    print("After function returns:")
    print("an_int:", an_int)
    print("a_list:", a_list)


if __name__ == "__main__":
    main()