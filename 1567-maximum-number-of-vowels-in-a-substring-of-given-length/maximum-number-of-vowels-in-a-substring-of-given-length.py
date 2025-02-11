class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}

        l = 0
        count = 0
        res = 0

        for r in range(len(s)):
            count +=1 if s[r] in vowel else 0
            if r - l +1 > k:
                count -=1 if s[l] in vowel else 0
                l +=1
            res = max(res,count)
        return res
        