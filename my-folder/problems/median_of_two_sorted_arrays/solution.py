class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3= nums1+nums2
        num3.sort()
        n=len(num3)
        if(n%2==0):
            return (num3[n//2]+num3[(n//2)-1])/2
        return num3[n//2]
        