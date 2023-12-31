class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin_index= 0
        end_index=len(nums)
        while(begin_index<end_index):
            midpoint= begin_index+(end_index-begin_index)//2
            midpoint_val= nums[midpoint]
            
            if(midpoint_val>= target):
                if midpoint_val== target:
                    return midpoint
                end_index= midpoint
            elif midpoint_val> target:
                end_index= midpoint-1
            else:
                begin_index= midpoint+1
        # for i in range(len(nums)):
        #     if nums[i]== target or nums[i]>target:
        #         return i
        return begin_index