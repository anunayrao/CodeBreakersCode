class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        N = len(s)
        start = -1
        result = 0
        window = set()
        for i in range(len(s)):
            if s[i] in window:
                start+=1
                while s[start] != s[i] and start < i:
                    window.remove(s[start])
                    start += 1
            window.add(s[i])
            result = max(result, i - start)
        return result
        