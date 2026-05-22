class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for num in nums:
            length = 1
            number = num
            while number - 1 in sett:
                length += 1
                number -= 1
            longest = max(longest, length)

        return longest
            

