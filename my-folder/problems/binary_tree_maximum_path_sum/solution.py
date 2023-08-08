# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]

        def dfs(root):
            if not root:
                return 0
            mleft= max(dfs(root.left), 0) #for handling the negative value nodes
            mright= max(dfs(root.right), 0)

            #print(left, right)

            res[0]= max(res[0], root.val+mleft+mright)
            #print(res[0])

            return root.val+ max(mleft, mright)
        dfs(root)

        return res[0]