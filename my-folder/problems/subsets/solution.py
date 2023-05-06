class Solution:

    def recfun(self, index, psunset, n, temp, result):

        if(index==n):
            result.append(psunset[:])
            return
        psunset.append(temp[index])
        self.recfun(index+1, psunset, n, temp, result)
        psunset.pop()
        self.recfun(index+1, psunset, n, temp, result)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        i=0
        self.recfun(i,[], n, nums,result)
        return result
