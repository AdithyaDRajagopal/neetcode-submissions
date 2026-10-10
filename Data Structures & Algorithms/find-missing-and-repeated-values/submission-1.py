class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        s = set()
        res = []
        actualSum = 0

        for i in range(n):
            for j in range(n):
                actualSum += grid[i][j]
                if grid[i][j] in s:
                    res.append(grid[i][j])
                s.add(grid[i][j])
        
        expectedSum = (n * n * (n * n + 1))// 2
        print(actualSum)
        print(expectedSum)
        res.append(expectedSum - actualSum + res[0])

        return res