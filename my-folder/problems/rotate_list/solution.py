
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ll=1
        temp=head
        if temp==None or temp.next==None or k==0:
            return head
        
        while temp.next!=None:
            ll+=1
            temp=temp.next
        
        k=k%ll
        k=ll-k

        temp.next=head
        while(k):
            k-=1
            temp=temp.next
            
        
        head=temp.next
        temp.next=None
        #print()
        return head
