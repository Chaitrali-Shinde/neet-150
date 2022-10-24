class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()
        s=s.lstrip()
        str1= s.split(" ")
        res=str1[len(str1)-1]
        return len(res)
        