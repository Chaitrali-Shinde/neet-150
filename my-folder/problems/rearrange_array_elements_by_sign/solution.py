class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if(i<0):
                neg.append(i)
            else:
                pos.append(i)
        print(neg)
        print(pos)
        i=len(nums)*2
        result=[]
        
        for i in range (0, len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result