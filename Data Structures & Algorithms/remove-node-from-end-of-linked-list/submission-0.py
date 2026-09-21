# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        nums = []
        curr = head

        while curr:
            nums.append(curr)
            curr = curr.next
        
        #find the index of node to remove
        index = len(nums) - n

        if index == 0:
            return head.next
        
        #remove the node, 
        #the number before the the index we trying to remove will be pointing to the next after the number on that index
        nums[index-1].next = nums[index].next
        return head