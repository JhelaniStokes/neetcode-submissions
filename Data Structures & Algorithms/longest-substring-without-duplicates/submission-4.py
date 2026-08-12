class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l=r=0
        seen = set()
        res = 1

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            res = max(res, r-l+1)
            seen.add(s[r])
            r+=1
        
        return res