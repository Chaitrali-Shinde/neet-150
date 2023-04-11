class Solution:
    def dfs(self, row, col, grid, visited, delrow, delcol):
        visited[row][col]=1
        m= len(grid)
        n= len(grid[0])

        for i in range(4):
            nrow= row+delrow[i]
            ncol= col+delcol[i]
            if 0<=nrow<m and 0<=ncol<n and visited[nrow][ncol]==0 and grid[nrow][ncol]==1:
                self.dfs(nrow, ncol, grid, visited, delrow, delcol)
        


    def numEnclaves(self, grid: List[List[int]]) -> int:

        m= len(grid)
        n= len(grid[0])

        visited= [[0 for i in range(n)] for i in range(m)]
        delrow= [-1,0, 1, 0]
        delcol=[0, -1, 0, 1]

        cnt=0

        for i in range(m):
            if grid[i][0]==1 and visited[i][0]==0:
                self.dfs(i, 0, grid, visited, delrow, delcol)
            if grid[i][n-1]==1 and visited[i][n-1]==0:
                self.dfs(i, n-1, grid, visited, delrow, delcol)
        
        for i in range(n):
            if grid[0][i]==1 and visited[0][i]==0:
                self.dfs(0, i, grid, visited, delrow, delcol)
            if grid[m-1][i]==1 and visited[m-1][i]==0:
                self.dfs(m-1, i, grid, visited, delrow, delcol)
        

        #for non-boundry numbers
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and visited[i][j]==0):
                    cnt+=1
        

        return cnt

        

