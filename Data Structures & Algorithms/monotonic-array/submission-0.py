class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        if n <= 1:
            return True

        order = "inc" if nums[0] <= nums[-1] else "dec"

        for i in range(1, n):
            if order == "inc":
                if nums[i] < nums[i-1]:
                    return False
            
            elif nums[i] > nums[i-1]:
                return False
        
        return True