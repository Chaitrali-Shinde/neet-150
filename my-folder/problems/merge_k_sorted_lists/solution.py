# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node= ListNode()
        nums=[]
        for i in lists:
            print(i)
            while i!= None:
                print(i.val)
                nums.append(i.val)
                i= i.next
            
        nums.sort()
        curr= node
        for i in nums:
            new_node= ListNode(i)
            while(curr.next!= None):
                curr= curr.next
            curr.next= new_node

        return node.next