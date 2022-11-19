class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin_index=0
        end_index= len(nums)-1
        while (begin_index<= end_index):
            midpoint= begin_index+(end_index-begin_index)//2
            midpoint_val= nums[midpoint]
            if(midpoint_val== target):
                return midpoint
            if nums[begin_index]<=nums[midpoint]:
                if nums[begin_index]<=target and nums[midpoint]>=target:
                    end_index= midpoint-1
                else:
                    begin_index= midpoint+1
            else:
                if(nums[midpoint]<=target and nums[end_index]>=target):
                    begin_index= midpoint+1
                else:
                    end_index= midpoint-1
        return -1



