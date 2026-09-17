class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1 
        area = 0
        while left < right:
            a = min(heights[left], heights[right]) * (right - left)
            area = max(a, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area            
            

            
        