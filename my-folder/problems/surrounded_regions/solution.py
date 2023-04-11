class Solution:
    def dfs(self, row, col, board, visited, delrow, delcol):
       # m is row
        m= len(board)
        #n is col
        n= len(board[0])
        visited[row][col]=1
        for i in range(4):
            nrow= row+delrow[i]
            ncol= col+delcol[i]
            if(0<=nrow<m and 0<=ncol<n and visited[nrow][ncol]==0 and board[nrow][ncol]=='O'):
                self.dfs(nrow, ncol, board, visited, delrow, delcol)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # m is row
        m= len(board)
        #n is col
        n= len(board[0])
        print(m,n)
        visited= [[0 for i in range(n)] for j in range(m)]
        #print(visited)
        delrow=[-1, 0, 1, 0]
        delcol=[0, -1, 0, 1]

        #check for boundry 0's and call dfs to marke them as visited, as we are not going to make them X
        
        for i in range(0, m):
            if(board[i][0]=='O' and visited[i][0]==0):
                self.dfs(i, 0, board, visited, delrow, delcol)
            if(board[i][n-1]=='O' and visited[i][n-1]==0):
                self.dfs(i, n-1, board, visited, delrow, delcol)
        

        for i in range(0,n):
            if(board[0][i]=='O' and visited[0][i]==0):
                self.dfs(0, i, board, visited, delrow, delcol)
            if(board[m-1][i]=='O' and visited[m-1][i]==0):
                self.dfs(m-1,i, board, visited, delrow, delcol)
        
        for i in range(m):
            for j in range(n):
                if(board[i][j]=='O' and visited[i][j]==0):
                    board[i][j]='X'
