class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            width = r - l
            height_val = min(height[r], height[l])
            area = width * height_val
            max_water = max(area,max_water)
            if height[l] < height[r]:
               l+=1
            else :
                r-=1
        return max_water