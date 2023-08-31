class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # N= m+n-2
        # r= m-1
        # res=1
        # for i in range(1, r + 1):
        #     res = res * (N - r + i) / i
        # return int(res)

        row= [1]*n
        #calculate values for remaining rows (rows other than last row)
        for i in range(m-1):
            newRow= [1]*n
            for j in range(n-2,-1, -1):
                newRow[j]= newRow[j+1]+row[j]
            row= newRow
        return row[0]
