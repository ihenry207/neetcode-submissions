# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)# initiate dummy nide and next is pointing to head
        groupPrev = dummy
        while True:
            Kth = self.getKth(groupPrev, k)#get kth element
            if not Kth:
                break # reached the end
            groupNext = Kth.next
            
            #reverse linkedlist
            prev, curr = Kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            #this is the kost confusing part
            tmp = groupPrev.next
            groupPrev.next = Kth
            groupPrev = tmp
        return dummy.next




        

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

        