class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max=0
        cnt=0
        for i in range(0, len(nums)):
            if(nums[i]==1):
                cnt+=1
            elif(nums[i]==0):
                if(cnt>max):
                    max=cnt
                cnt=0
        if(max>cnt):
            return max
        return cnt
    
            
        