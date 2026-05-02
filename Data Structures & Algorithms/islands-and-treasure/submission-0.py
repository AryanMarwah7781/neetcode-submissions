class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        INF = 2147483647

        def bfs(r,c):
            q = deque()
            visited = [[False] * COLS for _ in range(ROWS)]

            visited[r][c] = True
            q.append((r,c))

            distance = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    
                    if grid[row][col] == 0: # found treasure
                        grid[r][c] = distance
                        return

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (nr in range(ROWS) and
                            nc in range(COLS) and
                            visited[nr][nc] == False and
                            grid[nr][nc] != -1):
                                visited[nr][nc] = True
                                q.append((nr,nc))
                distance += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    bfs(r,c)

