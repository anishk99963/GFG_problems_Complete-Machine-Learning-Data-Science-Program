# You are given a String S, you need to print its characters at even indices(index starts at 0).

def utility():
    #The line below takes input. Don't change it!
    s=input().strip()
    
    
    for i in range(0,len(s),2): ## from 0 to length of str and skip 2
        print(s[i], end="")##printing character and separating characters by nothing
