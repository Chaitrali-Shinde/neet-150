class Solution:
    def findPeakGrid(self, matrix: List[List[int]]) -> List[int]:
        begin=0
        end= len(matrix[0])-1

        while begin <= end:
            maxRow=0
            mid= (begin+end)//2

            for row in range(len(matrix)):

                maxRow = row if (matrix[row][mid] >= matrix[maxRow][mid]) else maxRow

            leftBig = mid-1 >= begin  and  matrix[maxRow][mid-1] > matrix[maxRow][mid]
            RightBig = mid+1 <= end    and  matrix[maxRow][mid+1] > matrix[maxRow][mid]
            if (not leftBig) and (not RightBig):
                return [maxRow, mid]
            elif RightBig:             
                begin = mid+1     
            else:                          
                end = mid-1

        return []

        # startCol = 0
        # endCol = len(mat[0])-1
       
        # while startCol <= endCol:
        #     maxRow = 0
        #     midCol = (endCol+startCol)//2
            
        #     for row in range(len(mat)):
        #         maxRow = row if (mat[row][midCol] >= mat[maxRow][midCol]) else maxRow
            
        #     leftIsBig    =   midCol-1 >= startCol  and  mat[maxRow][midCol-1] > mat[maxRow][midCol]
        #     rightIsBig   =   midCol+1 <= endCol    and  mat[maxRow][midCol+1] > mat[maxRow][midCol]
            
        #     if (not leftIsBig) and (not rightIsBig):   # we have found the peak element
        #         return [maxRow, midCol]
        #     elif rightIsBig:             # if rightIsBig, then there is an element in 'right' that is bigger than all the elements in the 'midCol', 
        #         startCol = midCol+1     # so 'midCol' cannot have 'peakPlane'
        #     else:                           # leftIsBig
        #         endCol = midCol-1
                
        # return []