class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
#         char1= list(s)
#         char2= list(t)
#         if(len(s)==len(t)):
#             dic1={}
#             dic2={}
#             for i in char1:
#                 if i in dic1:
#                     val=dic1.get(i)
#                     dic1[i]= val+1
#                 else:
#                     dic1[i]=1
#             for i in char2:
#                 if i in dic2:
#                     val=dic2.get(i)
#                     dic2[i]= val+1
#                 else:
#                     dic2[i]=1
            
#             dict(sorted(dic2.items(), key=lambda item: item[1]))
#             dict(sorted(dic2.items(), key=lambda item: item[1]))
#             val1= list(dic1.values())
#             val2= list(dic2.values())
#             print(val1)
#             print(val2)
#             if(val1!=val2):
#                 return False
            
#             return True
    
#         return False
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
            print(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False