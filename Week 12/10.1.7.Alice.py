def unique_words(filename):
    myfile = open(filename, 'r')
    read_file = myfile.read()
    List_of_words = read_file.split()
    set_of_words = set()

    for word in List_of_words:
        set_of_words.add(word.lower())
    print(set_of_words)

    count_words = len(List_of_words)
    print(count_words)
    
    count_unique_words = len(set_of_words)
    print(count_unique_words)

def main():
    unique_words("C:\\Users\\sonab\\Downloads\\alice.txt")
main()