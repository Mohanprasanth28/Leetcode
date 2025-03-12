class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0:
            return len(nums)
        neg = 0
        zero = 0
        pos = 0
        for num in nums:
            if num < 0:
                neg += 1
            if num == 0:
                zero +=1
            if num > 0:
                pos = len(nums) - (neg+zero)
                break
        return max(neg,pos)

        