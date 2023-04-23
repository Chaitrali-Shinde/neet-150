class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        

        Snums= list(map(str, nums))
        print(Snums)
        Snums.sort(key=lambda x:x*9, reverse=True)
        output = ''.join(Snums)
        if all(ele=="0" for ele in output):
            return "0"
        return output