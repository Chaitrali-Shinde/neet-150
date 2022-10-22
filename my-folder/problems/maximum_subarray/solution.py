class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sub=0
        if(len(nums)==1):
            return nums[0]
        for i in range(0, len(nums)):
            sub+=nums[i]
            maxi= max(maxi, sub)
            if(sub<0):
                sub=0
            
                    
                    
        return maxi