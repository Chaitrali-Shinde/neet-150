class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r= 0,len(nums)-1
        while l<=r:
            mid= (l+r)//2
            if target== nums[mid]:
                return mid
            
            #left sorted portion
            if nums[l]<=nums[mid]:
                if target< nums[l] or target> nums[mid]:
                    l= mid+1
                    
                else:
                   r= mid-1
            
            #right sorted portion
            else:
                if target<nums[mid] or target >nums[r]:
                    r= mid-1
                else:
                    l= mid+1 
        
        return -1
                










        # while (l<= r):
        #     mid= l+(r-l)//2
        #     mid_val= nums[mid]
        #     if(mid_val== target):
        #         return mid
        #     if nums[l]<=nums[mid]:
        #         if nums[l]<=target and nums[mid]>=target:
        #             r= mid-1
        #         else:
        #             l= mid+1
        #     else:
        #         if(nums[mid]<=target and nums[r]>=target):
        #             l= mid+1
        #         else:
        #             r= mid-1
        # return -1



