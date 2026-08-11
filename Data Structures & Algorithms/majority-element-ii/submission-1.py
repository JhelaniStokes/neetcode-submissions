class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = math.floor(len(nums)/3)
        res = set()
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen[num] > n:
                res.add(num)
        
        return list(res)

