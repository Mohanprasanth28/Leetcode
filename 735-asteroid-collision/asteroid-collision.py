class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for num in asteroids:
            
            while res and num < 0 and res[-1] > 0:
                if abs(num) > res[-1]:
                    res.pop()
                    continue 
                elif abs(num) == res[-1]:  
                    res.pop()  
                break
            else:
                res.append(num)
        return res


        