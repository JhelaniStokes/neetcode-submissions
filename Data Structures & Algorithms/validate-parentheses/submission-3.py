class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parmap = {'[':']', '{':'}', '(':')'}

        for c in s:
            if c in parmap.keys():
                stack.append(c)
            else:
                if not stack or parmap[stack.pop()] != c:
                    return False
        
        return not stack
        