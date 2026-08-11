class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = set()
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > math.floor(n/3):
                res.add(num)
        
        return list(res)

