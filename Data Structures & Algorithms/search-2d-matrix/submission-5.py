class Solution:
    def searchInRow(self, matrix: List[List[int]], target:int, row: int) -> bool:
        st, end = 0, len(matrix[row]) - 1

        while st <= end:
            mid = st + (end - st)//2
            if target < matrix[row][mid]:
                end = mid - 1
            elif target > matrix[row][mid]:
                st = mid + 1
            else:
                return True
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        stR, endR = 0, len(matrix) - 1
        n = len(matrix[0])

        while stR <= endR:
            midR = stR + (endR - stR)//2

            if target >= matrix[midR][0] and target <= matrix[midR][n-1]:
                return self.searchInRow(matrix, target, midR)
            elif target < matrix[midR][0]:
                endR = midR - 1
            else:
                stR = midR + 1

        return False