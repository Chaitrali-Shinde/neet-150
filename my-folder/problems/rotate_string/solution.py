class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(0, len(goal)):
            s= s[-1]+s[0:-1]
            if s==goal:
                return True
        return False