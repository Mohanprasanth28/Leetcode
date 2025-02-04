class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        sum = 0
        a = []
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                sum += nums[i]
            else:
                a.append(sum + nums[i])
                sum = 0
        a.append(sum + nums[-1])
        return max(a)

        