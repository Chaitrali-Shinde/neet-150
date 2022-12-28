# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        temphead=head
        while(list1!=None and list2!= None):
            
            if(list1.val>list2.val):
                newNode= ListNode(list2.val, None)
                temphead.next=newNode
                temphead=temphead.next
                print(list2.val)
                list2= list2.next
                
            else:
                newNode= ListNode(list1.val, None)
                temphead.next=newNode
                temphead=temphead.next
                print(list1.val)
                list1= list1.next
        if list1==None:
            temphead.next=list2
        else:
            temphead.next=list1
        return head.next
        