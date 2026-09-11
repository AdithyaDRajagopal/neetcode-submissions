class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            triangleRow = [1] * (row + 1)
            if row > 0:
                lastRow = triangle[-1]
                for col in range(1, len(lastRow)):
                    triangleRow[col] = lastRow[col] + lastRow[col-1]
            
            triangle.append(triangleRow)

        return triangle