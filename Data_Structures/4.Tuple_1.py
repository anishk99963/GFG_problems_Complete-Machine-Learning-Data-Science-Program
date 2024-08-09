# You are given a tuple numbers that contains integers. You need to return a tuple containing doubles of given numbers.

def doubleTup(numbers):
    
    #holds 2*number 
    #Finally retrn the tuple
    temp = ()
    for i in numbers:
        temp = temp + (i*2,)
        
    return temp