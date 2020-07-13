class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)<3:
            return []
        
        nums.sort()
        result= []
        i = 0
        while i < len(nums):
            
            if i>0:
                while i < len(nums) and nums[i]==nums[i-1]:
                    i += 1
            
            j = i + 1
            k = len(nums) - 1
            
            while j<k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j]==nums[j-1]:
                        j += 1
                    while k > j and nums[k]==nums[k+1]:
                        k -= 1
            i += 1
        return result
    
    
    '''
    Runtime Complexity: O(n^2)
    Space Complexity : O(1)
    '''
                        
                    