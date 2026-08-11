class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_contains = {}
        t_contains = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_contains[s[i]] = s_contains.get(s[i], 0) + 1
            t_contains[t[i]] = t_contains.get(t[i], 0) + 1
        
        return s_contains == t_contains