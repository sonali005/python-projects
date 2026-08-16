import arrays

def making_arrays():
    array_a = arrays.Array(5)
    print(array_a)
    array_b = arrays.Array(1,0)
    print(array_b)
    array_c = arrays.Array(10, "")
    print(array_c)
    array_d = arrays.Array(20, False)
    print(array_d)

def main():
    making_arrays()

if __name__ == "__main__":
    main()