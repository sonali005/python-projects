def ascii_val(a_string):
    ord_list = []
    sentence_list = []
    em_string = ''
    for char in a_string:
        print(char, ord(char))
        ord_list.append(ord(char))
    #print(ord_list)


    for element in ord_list:
        sentence_list.append(chr(element))
    
    for letter in sentence_list:
        em_string += letter
    
    print(em_string)


def decode(encoded_message):
    
    decoded = ''

    for element in encoded_message:
        decoded += chr(element)
    
    print(decoded)

def main():
    a_string = 'I love GCIS123'
    #ascii_val(a_string)
    to_decode = [66,101,32,115,117,114,101,32,116,111,32,100,114,105,110,107,32,121,111,117,114,32,79,118,97,108,116,105,110,101,46]
    decode(to_decode)
 
if __name__ == '__main__':
    main()