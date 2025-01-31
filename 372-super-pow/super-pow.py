class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        c = ""
        for i in b:
            c +=str(i)
        result = pow(a,int(c),1337)
        return result
        

        