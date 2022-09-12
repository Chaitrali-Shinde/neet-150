class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        rev=str(x)
        rev= rev[::-1]
        if(x==int(rev)):
            return True
        
        return False
        