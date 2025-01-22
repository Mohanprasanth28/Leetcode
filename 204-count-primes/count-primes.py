class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        if n == 3:
            return 1
        num = [True] * (n)
        num[0] = num[1] = False
        p = 2 
        while p*p < n:
            if num[p]:
                for i in range(p*p,n,p):
                    num[i] = False
            p +=1
        count = 0
        for i in range (n):
            if num[i]:
                count +=1
        return count
        
        