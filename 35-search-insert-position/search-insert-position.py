class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        first = 0
        last = n - 1
        
        while first <= last:
            mid = (last+first) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid 
        