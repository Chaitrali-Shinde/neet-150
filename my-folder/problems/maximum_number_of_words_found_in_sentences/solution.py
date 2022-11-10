class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        m=0
        for i in s:
            l= i.split()
            if m<len(l):
                m= len(l)
        return m