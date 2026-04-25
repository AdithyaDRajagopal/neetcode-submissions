class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = (r - l) * minHeight
            if minHeight == heights[l]:
                l += 1
            else:
                r -= 1
            maxArea = max(area, maxArea)

        return maxArea