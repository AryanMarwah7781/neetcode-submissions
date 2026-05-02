class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_rows = len(grid)
        max_cols = len(grid[0])
        
        def dfs(row: int, col: int) -> int:
            # 1) boundary or water check
            if (
                row < 0 or row >= max_rows or
                col < 0 or col >= max_cols or
                grid[row][col] == 0
            ):
                return 0
            
            # 2) mark current cell visited
            grid[row][col] = 0
            
            # 3) start area count with this cell
            area = 1
            area += dfs(row-1, col)
            area += dfs(row+1, col)
            area += dfs(row, col-1)
            area += dfs(row, col+1)
            return area
        
        max_area = 0
        # 4) scan every cell, launch DFS on unvisited land
        for i in range(max_rows):
            for j in range(max_cols):
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)
        
        return max_area

        