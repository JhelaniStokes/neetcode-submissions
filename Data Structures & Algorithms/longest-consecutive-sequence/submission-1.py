class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items = set(nums)
        res = 0

        for num in items:
            if num - 1 not in items:
                cur = num
                while cur+1 in items:
                    cur += 1
                res = max(res, cur-num+1)
        return res

                    
        