class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROW=len(grid)
        COL=len(grid[0])
        max_ar=0
        def bfs(i,j):
            queue1=deque([(i,j)])
            delta=[(1,0),(-1,0),(0,1),(0,-1)]
            grid[i][j]=0
            res=1
            while queue1:
                row,col=queue1.popleft()
                for dr,dc in delta:
                    nr,nc=dr+row,dc+col
                    if (nr < 0 or nc < 0 or nr >= ROW or
                            nc >= COL or grid[nr][nc] == 0
                        ):
                            continue
                    queue1.append((nr,nc))
                    grid[nr][nc]=0
                    res+=1
            return res


        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    max_arr=bfs(i,j)
                    max_ar=max(max_arr,max_ar)
        return max_ar
