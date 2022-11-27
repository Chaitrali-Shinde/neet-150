import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftK=1
        rightK= max(piles)
        result=[]
        while(leftK<=rightK):
            midK=(leftK+rightK)//2
            hours=0
            for i in piles:
                hours+= i//midK
                if(i%midK!=0):
                    hours+=1
        
            if hours<=h:
                rightK= midK-1
            else:
                leftK= midK+1
    
        return leftK