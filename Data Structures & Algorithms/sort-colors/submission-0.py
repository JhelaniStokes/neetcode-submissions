class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        r = 0
        b = len(nums)-1
        i = 0
        while i <= b:
            if nums[i] == 0:
                swap(r, i)
                r += 1
                i += 1
            elif nums[i] == 2:
                swap(b, i)
                b -= 1
            else:
                i+=1



        """
        Do not return anything, modify nums in-place instead.
        """
        
