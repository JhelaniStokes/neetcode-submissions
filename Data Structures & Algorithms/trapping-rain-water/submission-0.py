class Solution:
    def trap(self, height: List[int]) -> int:
        max_r = 0
        max_l = 0

        l=0
        r = len(height)-1

        res=0
        while l < r:
            max_r = max(max_r, height[r])
            max_l = max(max_l, height[l])
            res += max(0, min(max_r, max_l)-min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res

        