class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(0, len(nums)):
            ans= target-nums[i]
            temp=nums[i]
            nums[i]=-1
            if ans in nums and nums[i]!=ans:
                result.append(i)
                result.append(nums.index(ans))
                return result
            nums[i]=temp
        return result