# Bitwise operators are useful when we want to work with bits. Here, we'll take a look at them.

# Given three positive integers a, b, and c. Your task is to perform some bitwise operations on them as given below:
# 1. d = a ^ a
# 2. e = c ^ b
# 3. f = a & b
# 4. g = c | (a ^ a)
# 5. h = ~e

def bitWiseOperation(a, b, c):
    # code here
    d = a ^ a
    e = c ^ b
    f = a & b
    g = c | (a ^ a)
    h = ~e
    
    print (d)
    print (e)
    print (f)
    print (g)
    print (h)
