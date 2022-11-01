class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False
        char1= list(s)
        char2= list(t)
        for i in char1:
            if(i in char2):
                j= char2.index(i)
                char2.pop(j)
            else:
                return False
        return True