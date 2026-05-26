class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxWindow = 0
        freq = {}
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(freq.values())
            window = r - l + 1

            if window - maxFreq > k:
                freq[s[l]] -= 1;
                l += 1
                window -= 1
                if not freq[s[l]]:
                    del freq[s[l]]

            maxWindow = max(maxWindow, window)

        return maxWindow