'''The following python code will write in a text file
1 - when you write in a while, always mention w mode
2 - remember that even if the file doesnt not exist, it will create a new file'''

def write_inFile(fileName, multilines):
    with open(fileName, 'w') as f:
        for line in multilines:
            f.write(line + '\n')



def main():
    fileName = "WrittenFile.txt"
    multilines= ["This is GCIS 123", "This is section 603", "Students need a lot to focus"]
    write_inFile(fileName, multilines)
if __name__ == "__main__":
    main()