class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        if len(nums) == 1 or k == 0:
            return

        count = len(nums)

        cur = 0
        prev = nums[0]
        start = 0
        while count > 0:
            nxt = (cur+k)%len(nums)
            tmp = nums[nxt]
            nums[nxt] = prev
            cur = nxt
            prev = tmp
            if cur == start:
                cur += 1
                start = cur
                prev = nums[cur]
            count -= 1







        