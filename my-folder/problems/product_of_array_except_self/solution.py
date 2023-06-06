class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #below written solution can be one approach but it's a brute force and it givens time limit exceeded.
        # result=[0]*len(nums)
        # for i in range(len(nums)):
        #     temp= nums[i]
        #     nums[i]=1
        #     result[i]= math.prod(nums)
        #     nums[i]= temp
        # return result
        
        #optimized approach
        prefix=[1]*len(nums)
        suffix= [1]*len(nums)
        temp=1
        for i in range(1, len(nums)):
            temp= temp*nums[i-1]
            prefix[i]=temp
        temp2=1
        for i in range(len(nums)-2, -1, -1):
            temp2= temp2*nums[i+1]
            suffix[i]=temp2
        result=[]
        for i in range(len(nums)):
            result.append(suffix[i]*prefix[i])
        return result



