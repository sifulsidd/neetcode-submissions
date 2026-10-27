class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for r in range(len(board)):
            for c in range(len(board[1])):
                if board[r][c] == ".":
                    continue
                rowCheck = "Row" + str(r) + str(board[r][c])
                colCheck = "Column" + str(c) + str(board[r][c])
                boxCheck = "box" + str(r//3) + str(c//3) + str(board[r][c])

                if rowCheck in row: 
                    return False
                if colCheck in col:
                    return False
                if boxCheck in box:
                    return False
                row[rowCheck] = True
                col[colCheck] = True
                box[boxCheck] = True
        
        return True
                