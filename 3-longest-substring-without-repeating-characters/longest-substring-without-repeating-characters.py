class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        arr = []
        for ch in s:
            if ch in arr:
                arr = arr[arr.index(ch)+1:]
                
            arr.append(ch)
            m = max(m,len(arr))
        return m


        