class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # multi-source bfs solution
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        INF = 2147483647

        q = collections.deque()
        visited = [[False] * COLS for _ in range(ROWS)]

        # start at the location of the treasure 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited[r][c] = True
        

        distance = 0
        
        while q:
            # for level-by-level bfs from the treasure, update the distance
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        visited[nr][nc] == False and
                        grid[nr][nc] != -1):
                            visited[nr][nc] = True
                            q.append((nr,nc))
            # level is over, increase by 1
            distance += 1


