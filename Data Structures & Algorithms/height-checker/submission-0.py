class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        expected = sorted(heights)

        count = 0
        for i in range(n):
            if expected[i] != heights[i]:
                count += 1

        return count