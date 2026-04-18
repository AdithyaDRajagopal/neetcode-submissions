class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0

        for num in nums:
            if num - 1 not in s:
                length = 1
                nextNum = num + 1
                while nextNum in s:
                    length += 1
                    nextNum += 1
                maxLen = max(maxLen, length)
        
        return maxLen
