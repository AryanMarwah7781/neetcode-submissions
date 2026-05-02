class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        max_R=len(grid)
        max_C=len(grid[0])
        island_c=0
        visited=set()
        def bfs(i,j):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q=deque()
            grid[i][j]="0"
            q.append((i,j))
            while q:
                row,col=q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= max_R or
                        nc >= max_C or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]="0"


        for i in range(0,max_R):
            for j in range(0,max_C):
                if grid[i][j] == "1":
                    bfs(i,j)
                    island_c+=1
        return island_c
                

        