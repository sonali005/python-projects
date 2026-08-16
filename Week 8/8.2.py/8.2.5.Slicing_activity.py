"""Write a function that slices a list of characters into words.
● Open your activities module and add a new function called “slices”.
○ Use your favorite search engine to look up a favorite lyric or quote and paste it 
into your new function as a string. Make sure that it doesn’t begin or end with a 
space.
○ Append the characters in the string to a list.
○ Use slicing to slice each individual word’s characters out of the list and print it.
○ You may hard code the indexes, but as a challenge try use a loop to find the index 
of whitespace and slice out the words.
● Call your function from main."""

def slices():
    string="Smooth like butter, like a criminal under cover"
    list_lyric=list(string)
    sliced_lyric=list_lyric[:]
    print(sliced_lyric)

def main():
    slices()

main()