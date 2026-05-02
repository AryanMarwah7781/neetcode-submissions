class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and 
                        nc in range(COLS) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1 and 
                    (r,c) not in visited):
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)

        return maxArea
