# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dumA=headA
        dumB=headB
        while(dumA!=dumB):
            if dumA==None:
                dumA=headB
            else:
                dumA=dumA.next
            if dumB==None:
                dumB=headA
            else:
                dumB=dumB.next
        return dumA
