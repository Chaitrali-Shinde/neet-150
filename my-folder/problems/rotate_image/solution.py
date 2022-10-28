class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #take transpose of the given matrix
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        
        
        n= len(matrix)-1
        for i in range(0, len(matrix)):
            l=matrix[i]
            l= l[::-1]
            matrix[i]=l               
