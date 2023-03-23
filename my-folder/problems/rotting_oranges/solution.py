class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        delrow=[-1,1,0,0]
        delcol=[0,0,-1, 1]
        q= []
        t=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==2 ):
                    q.append((i,j))
                    
        q.append(None)
        #print(q)

        while len(q)>1:
            popped_ele = q.pop(0)
            if popped_ele== None:
                t+=1
                q.append(None)
                continue
            r=popped_ele[0]
            c=popped_ele[1]
            
            for k in range(4):
                row=delrow[k]+r
                col=delcol[k]+c
                if(row>=0 and row<n and col>=0 and col<m and grid[row][col]==1):
                    q.append((row, col))
                    grid[row][col]=2

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1 
        return t