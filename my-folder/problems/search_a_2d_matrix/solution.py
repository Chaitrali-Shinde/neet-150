class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col=len(matrix), len(matrix[0])
        top ,bottom=0, row-1
        while top<= bottom:
            mid= (top+bottom)//2
            if target> matrix[mid][-1]:
               top= mid+1
            elif target <matrix[mid][0]:
                bottom= mid-1
            else:
                break

    #till here we found out the row in which the target is going to be, now we'll find the actual target

        if not (top<=bottom): return False

        row= (top+bottom)//2
        l, r=0, col-1
        while l<=r:
            m= (l+r)//2
            if target> matrix[row][m]:
                l= m+1
            elif target< matrix[row][m]:
                r= m-1
            else:
                return True
        

        return False


        
        
        