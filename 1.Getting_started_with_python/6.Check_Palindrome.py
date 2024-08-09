# You are given a number n. You need to see if the number is a palindrome or not (recursively)

class Solution:
    def isPalin(self,N):
        #code here
        def checkP(n, st, ed):
            if st >= ed:
                return True
            if n[st] != n[ed]:
                return False
            return checkP(n, st+1, ed-1)
        
        n = str(N)
        return checkP(n, 0, len(n)-1)