class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        begin_index=0
        end_index= len(nums)-1

        if(len(nums)==1):
            return nums[0]
        if(nums[0]!=nums[1] and len(nums)!=1):
            return nums[0]
        elif(nums[len(nums)-1]!= nums[len(nums)-2]):
            return nums[len(nums)-1]

        while(begin_index<=end_index):
            mid= begin_index+(end_index-begin_index)//2
            if(nums[mid]!= nums[mid-1] and nums[mid]!= nums[mid+1]):
                return nums[mid]
            if(mid%2==0 and nums[mid]== nums[mid+1] or mid%2==1 and nums[mid]== nums[mid-1]):
                begin_index= mid+1
            else:
                end_index= mid-1
        
        return -1
        