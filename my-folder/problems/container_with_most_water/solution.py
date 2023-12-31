class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l=0
        r= len(height)-1
        
        while l<r:
            res= (r-l)*min(height[l], height[r])
            area = max(area, res)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return area