import sys
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        prev= nums[0]
        for i in range(1, len(nums)):
            if(nums[i]==prev and nums[i]!= sys.maxsize):
                nums[i]=sys.maxsize
                n-=1
            elif(nums[i]!=sys.maxsize):
                prev=nums[i]
              
        nums.sort()
        return n