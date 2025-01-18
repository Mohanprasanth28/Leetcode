class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i , num in enumerate(nums):
            dif = target - num

            if dif in res:
                return [res[dif],i]
            
            res[num] = i
        