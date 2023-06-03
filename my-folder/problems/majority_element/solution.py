class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority= nums[0]
        cnt=1
        for i in range (1, len(nums)):
            if(majority== nums[i]):
                cnt+=1
            elif cnt==0:
                majority= nums[i]
            else:
                cnt-=1
        return majority
