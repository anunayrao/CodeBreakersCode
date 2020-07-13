class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        end = len(nums)-1
        maxjump = 0
        
        for idx,num in enumerate(nums):
            if maxjump >= end:
                return True
            
            if maxjump < idx:
                return False
            maxjump = max(maxjump,idx + nums[idx])
        
        return False