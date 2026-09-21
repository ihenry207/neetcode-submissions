# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = []
        for lst in lists:
            while lst:
                node.append(lst.val)
                lst = lst.next
        
        node.sort() # sort the node array we just had

        #transform that node back into linkedlist
        res = ListNode(0)#dummy linkedlist
        curr = res
        for n in node:
            curr.next = ListNode(n)
            curr = curr.next
        return res.next
        