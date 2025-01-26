class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        s = sum(nums)
        if s % 2 !=0:
            return 0
        count = 0
        left = 0
        for i in range(len(nums)-1):
            left += nums[i]
            right = s - left
            if (left - right) % 2 == 0:
                count +=1
        return count



        