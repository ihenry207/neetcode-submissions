"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #declare the copy Hasmap to store the linkedlist at
        OldToCopy = {None: None}#None poitning to none

        curr = head
        while curr:
            copy = Node(curr.val)
            OldToCopy[curr] = copy
            curr = curr.next
        
        #second pass
        curr = head
        while curr:
            copy = OldToCopy[curr]
            copy.next = OldToCopy[curr.next]
            copy.random = OldToCopy[curr.random]
            curr = curr.next

        return OldToCopy[head]