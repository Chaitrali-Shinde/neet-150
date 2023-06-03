class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row= len(matrix)
        col= len(matrix[0])
        l=0
        r= len(matrix)*len(matrix[0])-1
        while l<=r:
            mid= l+(r-l)//2
            if target== matrix[mid//col][mid%col]:
                return True
            elif target>matrix[mid//col][mid%col]:
                l= mid+1
            elif target<matrix[mid//col][mid%col]:
                r= mid-1



        return False


        
        
        