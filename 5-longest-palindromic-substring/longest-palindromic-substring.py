class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        st = ""
        for i in range(len(s)-1):
            low = i
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -=1
                high +=1
            string = s[low+1:high]
            if len(string) > len(st):
                st = string
            low = i
            high = i+1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -=1
                high +=1
                
            string = s[low+1:high]
            if len(string) > len(st):
                st = string
        return st
            
        