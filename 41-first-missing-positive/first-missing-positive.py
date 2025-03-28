class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        num = 0
        for i in range(0,len(nums)):
            if nums[i] > 0:
                num = i
                break 
        j = 1
        for i in range(num,len(nums)):
            if nums[i] != j:
                return j
            j += 1
        return j   




                

        