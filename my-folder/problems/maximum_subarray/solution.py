class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub=0
        maxSub= sum(nums)
        for i in nums:
            sub+=i
            maxSub= max(maxSub, sub)
            if sub<0:
                sub=0
        return maxSub