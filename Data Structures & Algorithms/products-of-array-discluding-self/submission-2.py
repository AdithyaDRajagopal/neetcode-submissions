class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i-1] = right[n-i] * nums[n-i]
        
        res= []
        for i in range(n):
            res.append(left[i] * right[i]) 
        return res