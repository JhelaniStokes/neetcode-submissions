class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        f1 = [0] * 26
        f2 = [0] * 26

        for c in s1:
            f1[ord(c)-ord('a')] += 1
        
        l = r = 0
        while r+1<len(s2) and r-l+1 < len(s1):
            f2[ord(s2[r])-ord('a')] += 1
            r+=1

        while r < len(s2):
            f2[ord(s2[r])-ord('a')] += 1
            if f1 == f2:
                return True
            f2[ord(s2[l])-ord('a')] -= 1
            l += 1
            r+=1
        
        return False
