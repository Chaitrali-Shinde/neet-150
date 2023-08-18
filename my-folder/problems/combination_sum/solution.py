class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []

        def dfs(i, curr, total):
            if total== target:
                res.append(curr.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            #left side of the recursion tree: add the candidate
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            #right side of the recursion tree: do not add the candidate
            curr.pop()
            dfs(i+1, curr, total)

        

        dfs(0, [], 0)
        return res