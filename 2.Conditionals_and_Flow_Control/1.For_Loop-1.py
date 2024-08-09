# You are given a number n, you need to print its multiplication table in a single line.

def utility():
    n=int(input())
    ## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i*n, end=" ") ## Separating by spaces using end =" "