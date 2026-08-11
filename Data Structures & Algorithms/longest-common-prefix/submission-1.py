class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        if len(strs) == 1:
            return strs[0]
        for i, c in enumerate(strs[0]):
            for j in range(1, len(strs), 1):
                if len(strs[j]) == i or strs[j][i] !=c:
                    return "".join(res)
            res.append(strs[j][i])

        return "".join(res)
