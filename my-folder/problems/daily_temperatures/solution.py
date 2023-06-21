class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result=[0]*len(temperatures)
        stack=[] #we will store [indexx, temp]

        for index, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackTemp, stackI= stack.pop()
                result[stackI]= (index-stackI)
            stack.append([t, index])
        
        return result