class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. One set per row (keys 0 through 8)
        row_sets = {i: set() for i in range(9)}

        # 2. One set per column (keys 0 through 8)
        col_sets = {j: set() for j in range(9)}

        # 3. One set per 3×3 box, indexed by (box_row, box_col) from (0,0) to (2,2)
        box_sets = {
            (bi, bj): set()
            for bi in range(3)
            for bj in range(3)
        }
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == ".":
                    continue 
                if board[i][j] in row_sets[i]:
                    return False
                if board[i][j] in col_sets[j]:
                    return False
                if board[i][j] in box_sets[(i//3,j//3)]:
                    return False
                row_sets[i].add(board[i][j])
                col_sets[j].add(board[i][j])
                box_sets[(i//3,j//3)].add(board[i][j])
        return True 
                        
                
        
        