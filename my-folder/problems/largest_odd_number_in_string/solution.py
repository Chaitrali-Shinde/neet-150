class Solution:
    def largestOddNumber(self, num: str) -> str:
        nums=int(num)
        while nums>0:
            if(nums%2!=0):
                return str(nums)
            else:
                nums= nums//10
        return ""
            