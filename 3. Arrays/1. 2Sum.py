class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        Pseudocode
        1. Take a dictionary to keep track of elements as keys and their indexes as values
        2. Now start iterating over the list and find the complement(target - num) and if the complements exists in dictionary then we have the result. 
        3. If not found then just return the empty list
        '''
        
        d = dict()
        
        for idx,num in enumerate(nums):
            c = target - num
            if c in d:
                return [d[c],idx]
            d[num] = idx
        
        return []
        