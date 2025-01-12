class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        len1 = Counter(s)
        len2 = Counter(t)
        return len1 == len2