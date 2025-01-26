class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        s = set()
        for char in count.values():
            if char in s:
                return False
            else:
                s.add(char)
        return True
        