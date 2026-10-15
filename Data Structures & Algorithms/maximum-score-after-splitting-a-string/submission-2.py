class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros, ones = [0] * n, [0] * n

        for i in range(n):
            res = 1 if s[i] == "0" else 0
            if i == 0:
                zeros[i] = res
            else:
                zeros[i] = zeros[i-1] + res
        
        for i in range(n-1, -1, -1):
            res = 1 if s[i] == "1" else 0
            if i == n-1:
                ones[i] = res
            else:
                ones[i] = ones[i+1] + res
        
        maxScore = 0
        for i in range(1, n):
            maxScore = max(maxScore, zeros[i-1] + ones[i])
        
        return maxScore