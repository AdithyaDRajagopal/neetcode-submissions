class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)

        for num in nums:
            idx = min(num, len(nums))
            count[idx] += 1
        
        right = 0
        for i in range(len(nums), -1, -1):
            right += count[i]
            if i == right:
                return i

        return -1