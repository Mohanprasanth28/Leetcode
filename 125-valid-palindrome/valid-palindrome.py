class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.lower() for s in s if s.isalnum())
        
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start +=1
            end -=1
        return True

        