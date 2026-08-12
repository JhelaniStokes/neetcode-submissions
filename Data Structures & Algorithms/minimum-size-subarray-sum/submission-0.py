class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1

        l=r=0

        tot = 0
        while r < len(nums):
            tot += nums[r]
            if tot >= target:
                res = min(res, r-l+1)
            while tot > target and l < r:
                tot -= nums[l]
                l += 1
                if tot >= target:
                    res = min(res, r-l+1)
            r += 1
        if res == len(nums)+1:
            return 0
            
        
        return res




        