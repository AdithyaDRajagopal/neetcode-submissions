class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        odd = 0
        longest = 0
        for key in count:
            if count[key] % 2 == 0:
                longest += count[key]
            else:
                longest += (count[key] - 1)
                odd = 1
        
        return longest + odd