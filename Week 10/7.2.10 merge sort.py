def marge(seq1, seq2):
    i,j = 0,0
    result = ""

    while i<len(seq1) and j<len(seq2):
        if int(seq1[i]) < int(seq2[i]):
            result += seq1[i]
            i+=1
        else:
            result += seq2[j]
            j+=1
    
    result += seq1[i:]
    result += seq2[j:]
    return result

seq1 = "135"
seq2 = "246"

print("merged result: ", seq1 + seq2)