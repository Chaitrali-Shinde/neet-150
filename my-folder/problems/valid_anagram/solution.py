class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # approach 1
        # s= list(s)
        # t= list(t)

        # s.sort()
        # t.sort()
        # if s ==t:
        #     return True
        # return False
        # approach 2
        # return sorted(t)== sorted(s)

        # approach3
        countS, countT={}, {}
        if len(s)!= len(t): return False

        for i in range(len(s)):
            countS[s[i]]= 1+ countS.get(s[i], 0)
            countT[t[i]]= 1+ countT.get(t[i], 0)
        if countT!= countS:
            return False
        return True
            
