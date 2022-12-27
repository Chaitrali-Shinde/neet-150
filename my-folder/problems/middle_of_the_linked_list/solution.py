# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # len=1
        # temp=head
        # while(temp.next!=None):
        #     temp=temp.next
        #     len+=1
        # len=len//2
        # result=head
        # while(len):
        #     result=result.next
        #     len-=1
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next
            if(fast!=None):
                fast=fast.next
        
        return slow
