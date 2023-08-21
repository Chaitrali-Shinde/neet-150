class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit= set()
        preMap= {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs]== []:
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            #eka recursion madhe toh visit zala ahe tr toh next cycle madhe ala tr visited disel which might give us wrong answer
            visit.remove(crs)
            #we have already gone through all the pre-req courses of the given ccourse and they can be completed so the current course can also be completed so instead of again going to all the pre-req we can tell the course doesn't have any pre-req we can complete the course directly
            preMap[crs]=[]


            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
