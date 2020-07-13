class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        start = -1
        mul = 1
        result = 0
        N = len(nums)

        for i in range(len(nums)):
            mul *= nums[i]
            while mul >= k and start < i:
                start += 1
                mul /= nums[start]
            
            
            result += i - start 
            
        return result
