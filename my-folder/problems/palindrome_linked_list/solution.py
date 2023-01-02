# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head==None or head.next==None): return True

        fast=head
        slow=head

        #find the mid of linked list
        while(fast.next!=None and fast.next.next!=None):
            fast=fast.next.next
            slow=slow.next
        
        #for reversing the second half of the linked list
        dummy=None
        nextNode=None
        rhead=slow.next
        while(rhead):
            nextNode=rhead.next
            rhead.next=dummy
            dummy=rhead
            rhead=nextNode

        slow.next=dummy
        slow=slow.next

        #check if palindrome
        
        while(slow):
            if(head.val!=slow.val):
                return False
            head=head.next
            slow=slow.next      
        
        return True
