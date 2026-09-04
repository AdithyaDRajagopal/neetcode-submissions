class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
                maxOnes = max(maxOnes, ones)
            else:
                ones = 0

        return maxOnes