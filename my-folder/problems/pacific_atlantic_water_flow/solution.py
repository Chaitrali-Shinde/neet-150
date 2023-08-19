class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:

        ROWS, COLS= len(height), len(height[0])
        pcf, atl= set(), set()
        res=[]

        def dfs(r, c, visit, prevHeight):
            if(r<0 or c<0 or r==ROWS or c== COLS or (r,c) in visit or height[r][c]<prevHeight ):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, height[r][c])
            dfs(r-1, c, visit, height[r][c])
            dfs(r, c+1, visit, height[r][c])
            dfs(r, c-1, visit, height[r][c])



        for c in range(COLS):
            dfs(0, c, pcf, height[0][c])
            dfs(ROWS-1, c, atl, height[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pcf, height[r][0])
            dfs(r, COLS-1, atl, height[r][COLS-1])


        for r in range (ROWS):
            for c in range(COLS):
                if ((r,c)in pcf and (r,c) in atl):
                    res.append((r,c))

        return res