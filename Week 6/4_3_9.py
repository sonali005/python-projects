def hello_world_reverse(string1):

    start = len(string1) - 1
    stop = -1
    step = -1

    for x in range(start, stop, step):
        print (string1[x], end="")
              
def main():

    hello_world_reverse("Hello World!")

if __name__ == "__main__":
    main()