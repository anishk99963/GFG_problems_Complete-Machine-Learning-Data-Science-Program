# Given a string s, you need to slice it so that the output is a substring that contains all the chracters except first and last. The length of the s will be greater than 2.

def sliceString(s):
    #Write your code below
    r = s[1:len(s)-1]
    return r