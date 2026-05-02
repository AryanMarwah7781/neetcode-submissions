class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        # fresh > 0 so that the loop doesn't keep running after
        # all the oranges are rotten - no counting extra minutes
        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        fresh -=1
            minutes += 1

        return minutes if fresh == 0 else -1