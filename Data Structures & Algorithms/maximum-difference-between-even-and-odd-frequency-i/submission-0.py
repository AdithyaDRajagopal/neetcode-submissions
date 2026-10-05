class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        oddMax, evenMin = 0, float("inf")
        for i in count.values():
            if i % 2 != 0:
                oddMax = max(oddMax, i)
            else:
                evenMin = min(evenMin, i)
        
        return oddMax - evenMin