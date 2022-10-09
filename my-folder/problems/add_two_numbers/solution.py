# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=""
        num2=""
        while l1.next!=None:
            num1+=(str(l1.val))
            l1=l1.next
        num1+=(str(l1.val))
        num1= num1[::-1]
        #print(num1)
        while l2.next!=None:
            num2+=(str(l2.val))
            l2=l2.next
        num2+=(str(l2.val))
        num2= num2[::-1]
        #print(num2)
        num3= int(num1)+ int(num2)    
        l3= ListNode()
        curr=l3
        if(num3==0):
            return l3
        
        while(num3>0):
            temp= num3%10
            curr.next=ListNode(temp)
            curr=curr.next
            num3= num3//10
        
        return l3.next
            
        
        
        