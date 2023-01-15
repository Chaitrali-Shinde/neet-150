class Solution:
    def dfs(self, adjLS, node, visit):
        visit[node]=True
        for i in adjLS[node]:
            if(visit[i]==False):
                self.dfs(adjLS, i, visit)



    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V= len(isConnected)
        adjLS = {i:[] for i in range(1, V+1)}
        cnt=0
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if(isConnected[i][j]==1 and i is not j):
                    adjLS[i+1].append(j+1)
        
        visit=[False]*(V+1)

        for City in range(1, V+1):
            if(visit[City]==False):
                cnt+=1
                self.dfs(adjLS, City, visit)

        return cnt