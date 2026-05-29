class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, suffix = [0]*n, [0]*n

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i-1])
            suffix[n-i-1] = max(suffix[n-i], height[n-i])

        totalArea = 0
        for i in range(n):
            area = min(prefix[i], suffix[i]) - height[i]
            if area > 0:
                totalArea += area
        
        return totalArea