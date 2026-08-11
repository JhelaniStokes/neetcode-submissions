class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i, x in enumerate(nums):
            if target - x in sum_map:
                return [sum_map[target-x], i]
            sum_map[x] = i

