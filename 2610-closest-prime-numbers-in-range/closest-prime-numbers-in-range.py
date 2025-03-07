class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime(left,right):
            arr = [True] * (right + 1)
            arr[0] , arr[1] = False, False

            for i in range(2,int(right**0.5)+1):
                if arr[i]:
                    for j in range(i*i,right+1,i):
                        arr[j] = False
            #prime = [num for num in range(arr) if arr[num] and i >= left]
            return [num for num in range(left, right + 1) if arr[num]]

        cl_prime = prime(left,right)


        if len(cl_prime) <= 1:
            return [-1,-1]
        a, b = cl_prime[0], cl_prime[1]
        for i in range(1,len(cl_prime)):
            if cl_prime[i] - cl_prime[i-1] < (b-a):
                a = cl_prime[i-1]
                b = cl_prime[i]    

        
        return [a,b]
        
        