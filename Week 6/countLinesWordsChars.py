'''this python code will count all the lines in a text file
and then it will count all the words in that file
and then will count all the charcaters in that file'''

def count_lines_words_charcaters(filePath):

    try:
    # open the file and read it
        with open(filePath, 'r') as f:
            lineCount = 0
            wordCount = 0
            characCount = 0

            for line in f:
                lineCount = lineCount + 1
                print(lineCount)
                words = line.strip().split()
                wordCount = wordCount + len(words)
                print(wordCount)
                characCount = characCount + len(line)
                print(characCount)
                print()

        print("Lines count: ", lineCount)
        print("Words count: ", wordCount)
        print("Characters count: ", characCount)
    except:
        print("File not found, please create the file")

def main():
    file_path = "intro.txt"
    count_lines_words_charcaters(file_path)
if __name__ == "__main__":
    main()