class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in s:
                    return False
                
                s.add(board[i][j])
        
        # Validate columns
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                
                if board[j][i] in s:
                    return False
                
                s.add(board[j][i])

        boxStart = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
        for row, col in boxStart:
            s = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == '.':
                        continue
                    
                    if board[i][j] in s:
                        return False
                    
                    s.add(board[i][j])

        return True
