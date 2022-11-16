class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxi= max(nums)
        return nums.index(maxi)