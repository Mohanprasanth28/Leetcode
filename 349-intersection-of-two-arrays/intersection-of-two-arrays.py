class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = set()
        i = 0
        for i in nums1:
            for j in nums2:
                if(i == j):
                    arr.add(j)
                
        return list(arr)
        