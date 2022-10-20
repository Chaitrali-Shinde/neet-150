class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        s=s.split(" ")
        for i in s:
            res= i+ " "+res
            res= res.rstrip()
            res= res.lstrip()
        return res