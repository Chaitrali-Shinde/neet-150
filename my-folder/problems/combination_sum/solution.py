class Solution:

    def subsets(self,index, tempSub, n, temp, result, target):
        if(index==n):
            if(target==0):
                result.append(tempSub[:])
            return 
        if(temp[index]<=target):
            tempSub.append(temp[index])
            self.subsets(index, tempSub, n, temp, result, target-temp[index])
            tempSub.pop()
        self.subsets(index+1, tempSub, n, temp, result, target)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result=[]
        n= len(candidates)
        i=0
        self.subsets(i, [], n, candidates, result, target)
        return result