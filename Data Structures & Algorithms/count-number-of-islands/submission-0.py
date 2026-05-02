class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and 
                        c in range(COLS) and
                        grid[r][c] == '1' and
                        (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands
