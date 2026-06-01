class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0 
        max_len = 0 
        for right in range(len(s)):
            if s[right] in mp and mp[s[right]] >= left:
                left = mp[s[right]] +1 
            mp[s[right]] = right 
            max_len = max(max_len, right- left+1)
        return max_len
        