class Solution:

    def palindrome(self,s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


    def subStrings(self,index, s, sub, result):

        if(index== len(s)):
            result.append(sub[:])
            return
        for i in range(index, len(s)):
            if(self.palindrome(s, index, i)):
                sub.append(s[index:i+1])
                self.subStrings(i+1, s, sub, result)
                sub.pop()
                

    def partition(self, s: str) -> List[List[str]]:

        sub=[]
        result=[]
        self.subStrings(0, s, sub, result)
        return result