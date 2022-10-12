class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total= sum(nums)
        left=0
        for i in range (len(nums)):
            total-=nums[i]
            if(left==total):
                return i
            left+=nums[i]
        return -1
        