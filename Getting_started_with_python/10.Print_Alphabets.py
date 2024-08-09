# Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2, separated by space, in a single line.

def alphabets(c1,c2):
    
    #Code below to print alphabets from c1 to c2
    # Don't provide a new line after printing
    i = chr
    for i in range(ord(c1),ord(c2)+1):
        print(chr(i), end=" ")