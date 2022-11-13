class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        target_position=[]
        Flag= False
        begin_index=0
        end_index= len(nums)
        while begin_index< end_index:
            midpoint= begin_index +(end_index- begin_index) //2
            midpoint_val= nums[midpoint]
            if midpoint_val>=target:
                if midpoint_val== target:
                    Flag= True
                end_index= midpoint
            else:
                begin_index= midpoint+1
        target_position.append(begin_index)

        begin_index=0
        end_index= len(nums)

        while begin_index< end_index:
            midpoint= begin_index +(end_index- begin_index) //2
            midpoint_val= nums[midpoint]
            if midpoint_val>target:
                end_index= midpoint
            else:
                begin_index= midpoint+1
        target_position.append(begin_index-1)
        
        if(Flag):
            return target_position
        
        return [-1, -1]