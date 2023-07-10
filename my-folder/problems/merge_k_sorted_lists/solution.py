# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # node= ListNode()
        # nums=[]
        # for i in lists:
        #     #print(i)
        #     while i!= None:
        #         #print(i.val)
        #         nums.append(i.val)
        #         i= i.next
        # #print(nums)
        # nums.sort()
        # curr= node
        # for i in nums:
        #     new_node= ListNode(i)
        #     while(curr.next!= None):
        #         curr= curr.next
        #     curr.next= new_node

        # return node.next

        if not lists or len(lists)== 0:
            return None

        while len(lists)>1:

            mergedList=[]
            for i in range( 0, len(lists), 2):
                l1= lists[i]
                l2= lists[i+1] if (i+1)<len(lists) else None
                mergedList.append(self.merge_lists(l1, l2))
            lists= mergedList
        
        return lists[0]

    def merge_lists(self, list1, list2):
        dummy= ListNode()
        tail= dummy

        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1= list1.next

            else:
                tail.next= list2
                list2= list2.next
            tail= tail.next

        if list1:
            tail.next= list1
        if list2:
            tail.next= list2

        return dummy.next











