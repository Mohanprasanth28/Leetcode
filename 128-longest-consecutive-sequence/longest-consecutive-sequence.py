class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest = 0
        for n in seq:
            if (n-1) not in seq:
                length = 1
                while (n+length) in seq:
                    length +=1
                longest = max(length,longest)
        return longest        