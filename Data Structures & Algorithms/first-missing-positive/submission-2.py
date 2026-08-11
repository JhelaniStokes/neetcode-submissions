class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
            elif nums[i] != nums[nums[i]-1]:
                targ = nums[i]-1
                nums[i], nums[targ] = nums[targ], nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums)+1
