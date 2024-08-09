# You are given a tuple numbers that contains a A.P sequence integer. You need to calculate the next three sequences of numbers and return the whole sequence in a tuple.

def sequence(numbers):
    
    ans = list(numbers)
    
    d = numbers[1] - numbers[0] # Calculate the common difference
    
    for _ in range(3):
        if d < 0:
            ans.append(ans[-1] - abs(d))
        else:
            ans.append(ans[-1] + abs(d))
    
    return tuple(ans)