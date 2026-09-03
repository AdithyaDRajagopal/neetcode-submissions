class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        area = 0
        l, r = 0, len(height) - 1

        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)

            if lmax < rmax:
                area += (lmax - height[l])
                l += 1
            else:
                area += (rmax - height[r])
                r -= 1
            
        return area
