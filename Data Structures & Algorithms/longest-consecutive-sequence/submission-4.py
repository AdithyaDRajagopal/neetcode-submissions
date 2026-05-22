class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in sett:
                length = 1
                nextNum = num + 1
                while nextNum in sett:
                    length += 1
                    nextNum += 1
                longest = max(longest, length)

        return longest
            

