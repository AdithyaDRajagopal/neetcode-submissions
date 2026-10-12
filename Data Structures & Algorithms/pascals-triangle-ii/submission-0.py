class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            if i == 1:
                row.append(1)
                continue

            newRow = [1] * (len(row) + 1)
            for r in range(1, len(row)):
                newRow[r] = row[r] + row[r-1]
            row = newRow

        return row
