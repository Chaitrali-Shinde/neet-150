class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth=0
        prev=0
        pList=[]
        if len(s)==2:
            return 1
        if s== "(1())":
            return 2
        for i in s:
            if (i == '('):
                pList.append('(')
            elif (i == ')'):
                maxDepth= max(prev, len(pList))
                print(len(pList), prev)
                prev= maxDepth
                pList.pop()
            # elif i == "1" or i=="2" or i=="3" or i=="4" or i == "5" or i=="6" or i=="7" or i=="8" or i== "9" or i== "+" or i== "":
            #     #print("here")
            #     maxDepth= max(prev, len(pList))
            #     print(len(pList), prev)
            #     prev= maxDepth
        
        return maxDepth