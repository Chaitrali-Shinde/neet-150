# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr= root

        while curr:
            #if the value of p,q is greater than current find in right tree or if less then in left tree
            if q.val>curr.val and p.val>curr.val:
                curr= curr.right
            elif q.val<curr.val and p.val<curr.val:
                curr= curr.left
            #if we go the splitting point of p and q then that node is the LAC
            else:
                return curr