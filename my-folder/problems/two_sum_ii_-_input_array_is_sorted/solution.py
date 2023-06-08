class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            #print(d)
            if r in d: 
                return [d[r]+1, i+1]
            d[j] = i