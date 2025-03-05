class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        arr = [0] * n
        l ,r = 0,n-1

        for i in range(n-1,-1,-1):
            if abs(nums[l]) > abs(nums[r]):
                val = nums[l]
                l +=1
            else:
                val = nums[r]
                r -=1
            arr[i] = val ** 2
        return arr
        