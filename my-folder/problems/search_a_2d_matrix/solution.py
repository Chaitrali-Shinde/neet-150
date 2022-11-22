class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range (0, len(matrix)):
        #     begin_index=0
        #     end_index= len(matrix[0])-1
        #     while(begin_index<=end_index):
        #         mid= begin_index+(end_index-begin_index)//2
        #         if(matrix[i][mid]==target):
        #             return True
        #         else:
        #             if(matrix[i][mid]>target):
        #                 end_index= mid-1
        #             else:
        #                 begin_index= mid+1
                        
        # return False

        c=len(matrix[0])
        r=len(matrix)
        l=0
        h=(c*r)-1
        while l<=h:
            m=l+(h-l)//2
            if matrix[m//c][m%c]==target:
                return True
            elif matrix[m//c][m%c]<target:
                l=m+1
            else:
                h=m-1
        return False
