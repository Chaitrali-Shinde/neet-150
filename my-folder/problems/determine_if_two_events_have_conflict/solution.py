class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        r1= int("".join(event1[0].split(":")))
        r2= int("".join(event1[1].split(":")))+1
        print(r1)
        print(r2)
        list1=list(range(r1, r2))
        ans= int("".join(event2[0].split(":")))
        ans2= int("".join(event2[1].split(":")))+1
        list2= list(range(ans, ans2))
        
        for i in list1:
            if i in list2:
                return True
        return False