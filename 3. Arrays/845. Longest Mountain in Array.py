class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        start = 0
        result = 0 
        N = len(A)
        
        while start < N:
            end = start
            if end + 1 < N and A[end] < A[end+1]:
                while end + 1 < N and A[end] < A[end+1]:
                    end += 1
            
                if end + 1 < N and A[end] > A[end+1]:
                    while end + 1 < N and A[end] > A[end+1]:
                        end += 1
                    result = max(result, end - start + 1)
            start = max(start+1, end)
        
        return result   
        
       