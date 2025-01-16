class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = 0

        for i, jump in enumerate(nums):
            if i > last:
                return False
            last = max(last, i + jump)
            if last >= len(nums) -1:
                return True

        return False
        