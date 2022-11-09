# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head==None):
            return head
        temp= head
        leni=0
        while(temp!= None):
            leni+=1
            temp=temp.next
        remove= (leni-n)
        if(remove==0):
            temp= head.next
            #head.next= None
            return temp
        curr= head
        prev=None
        while(remove>0):
            prev= curr
            curr= curr.next
            remove= remove-1
        prev.next= curr.next
        #print(prev.val, curr)
        return head



