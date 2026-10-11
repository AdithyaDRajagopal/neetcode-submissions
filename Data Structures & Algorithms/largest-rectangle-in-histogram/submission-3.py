class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left, right = [0] * n, [0] * n
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            right[i] = n if not stack else stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            maxArea = max(area, maxArea)

        return maxArea