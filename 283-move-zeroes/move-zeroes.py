class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] !=0:
                nums[i],nums[a] = nums[a],nums[i]
                a +=1

        