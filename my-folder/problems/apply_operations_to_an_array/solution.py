class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]= nums[i]*2
                nums[i+1]=0
        i=0
        j=0
        while(j<len(nums)):
            if(nums[i]==0):
                nums.pop(i)
                nums.append(0)
                i=i-1
            i+=1
            j=j+1
        print(nums)
        return nums
                