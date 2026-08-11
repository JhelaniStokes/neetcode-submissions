class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        suffix = nums.copy()

        res = [0]*len(nums)

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i]*prefix[i-1]
        
        for i in range(len(suffix)-2, -1, -1):
            suffix[i] = suffix[i]*suffix[i+1]
        
        for i in range(len(res)):
            if i+1 > len(res)-1:
                res[i] = prefix[i-1]
            elif i-1 < 0:
                res[i] = suffix[i+1]
            else:
                res[i] = prefix[i-1]*suffix[i+1]
        
        return res