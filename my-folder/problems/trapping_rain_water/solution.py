class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, res= 0, len(height)-1, 0
        lmax= height[l]
        rmax= height[r]

        while l<r:
            if lmax<rmax:
                l+=1
                lmax= max(lmax, height[l])
                res+= lmax- height[l]
            else:
                r-=1
                rmax= max(rmax, height[r])
                res+= rmax- height[r]
        return res