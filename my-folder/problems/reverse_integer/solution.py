class Solution:
    def reverse(self, x: int) -> int:
        flag=False
        if x<0:
            x=x*-1
            flag=True
        s= str(x)
        rev= s[::-1]
        x=int(rev)
        if flag==True:
            x=int(rev)*-1
        if abs(x) >= 2**31-1:
            return 0
        return x
        