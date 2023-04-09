class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m= len(mat)
        n= len(mat[0])
        dist=[[0 for j in range(n)] for i in range(m)]
        v=[[0 for j in range(n)] for i in range(m)]
        queue=deque()
       
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):
                    v[i][j]=1  
                    queue.append([i,j,0])
       
        while len(queue)>0:
            a,b,step=queue.popleft()
            
            for r,c in [(a,b-1),(a,b+1),(a-1,b),(a+1,b)]:
                if(0<=r<m and 0<=c<n and v[r][c]==0):
                    v[r][c]=1
                    dist[r][c]= step+1
                    queue.append([r,c,dist[r][c]])

                    
        return dist

