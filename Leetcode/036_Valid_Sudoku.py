# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if not num.isdigit():
                    continue
                    
                sq = (i//3, j//3)
                if num in row[i] or num in col[j] or num in square[sq]:
                    return False
                else:
                    row[i].add(num)
                    col[j].add(num)
                    square[sq].add(num)
        return True
                    

# OR

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)    # key = (r/3,c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                    
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3,c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                
        return True
        