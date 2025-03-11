class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atMostK(nums, k):
            left = 0
            count = 0
            odd_count = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1  

                while k < 0: 
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1

                count += (right - left + 1) 

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)



        