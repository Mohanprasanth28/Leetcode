class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr =[]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0
        count = 0
        for c in nums:
            if c != 0:
                arr.append(c)
            else:
                count +=1
        arr.extend([0]*count)
        return arr
        