class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tail = len(nums)
        head = 0 
        count = 0 
        if not nums:
            return 0
        while head < tail and head < len(nums):
            if nums[head] == val:
                tail -= 1
                nums[head] = nums[tail]
            else:
                head += 1
        

        
        
        return tail


        