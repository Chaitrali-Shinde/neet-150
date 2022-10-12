class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total= sum(nums)
        n= len(nums)
        nums1= nums.copy()
        nums1[n-1]= total
        for i in range(n-2, -1, -1):
            total= total-nums[i+1]
            nums1[i]= total
            
        return nums1