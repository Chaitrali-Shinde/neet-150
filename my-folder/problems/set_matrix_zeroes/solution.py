class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        for i in range(0,len(m)):
            for j in range(0,len(m[i])):
                if m[i][j]==0:
                    row.append(i)
                    col.append(j)
        for x in row:
            for i in range(0,len(m)):
                for j in range(0,len(m[i])):
                    if i==x:
                        m[i][j]=0
        for x in col:
            for i in range(0,len(m)):
                for j in range(0,len(m[i])):
                    if j==x:
                        m[i][j]=0
                