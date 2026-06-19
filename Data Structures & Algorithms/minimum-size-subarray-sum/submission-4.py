class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        l, total = 0, 0
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                window = r - l + 1
                length = min(length, window)
                l += 1
        
        return length if length <= len(nums) else 0



