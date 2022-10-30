class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        nums.sort()
        if(len(nums)==0):
            return 0
        cons=1;
        prev=0
        #print(nums)
        for i in range(0,len(nums)-1):
            if((nums[i]+1)==nums[i+1]):
                print(cons)
                cons+=1
            else:
                prev=max(prev, cons)
                print(prev)
                cons=1
        
        return max(prev, cons)