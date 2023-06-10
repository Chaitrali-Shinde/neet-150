class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        #i represents the index and j represent the actual number
        # dict[j: actual number]= i(index)
        # for i, j in enumerate(nums):
        #     #print(i, j)
        #     r = target - j
        #     #print(d)
        #     if r in d: 
        #         return [d[r]+1, i+1]
        #     d[j] = i


            #approach II: Time complexity: O(n), space complexity: O(1)
        l, r= 0, len(nums)-1
        while(l<r):
            resultS= nums[l]+nums[r]
            if resultS>target:
                r-=1
            elif resultS<target:
                l+=1
            else:
                return [l+1, r+1]
        
        return []

