class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        PseudoCode
        1. Base Case: if list has only one element then just return 1
        2. Take two pointers namely i and j. Use i in loop to iterate over to the list and use j to keep track of the position which needs to be filled with unique element.
        3. 
        
        '''
        
        if len(nums)==1:
            return 1
        
        j = 1
        for i in range(1,len(nums)):
            
            if(nums[i]!=nums[i-1]):
                nums[j] = nums[i]
                j += 1
            
        return j
            
        