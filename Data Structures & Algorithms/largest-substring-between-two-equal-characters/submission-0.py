class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstIdx = [-1] * 26
        longest = -1

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')

            if firstIdx[idx] == -1:
                firstIdx[idx] = i
            else:
                longest = max(longest, i - firstIdx[idx] - 1)
        
        return longest