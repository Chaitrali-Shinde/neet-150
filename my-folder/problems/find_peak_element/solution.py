class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        if len(nums)==2:
            if(nums[0]> nums[1]):
                return 0
            else:
                return 1
        begin_index=0
        end_index=len(nums)-1
        while(begin_index<end_index):
            mid= begin_index+(end_index-begin_index)//2
            if(nums[mid]<nums[mid+1]):
                begin_index= mid+1
            else:
                end_index= mid
        
        return begin_index