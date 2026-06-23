# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, node = None, head

        # continue iterating until there is no more nodes left in the list
        while node: 
            # reverse 2 pointers
            temp = node.next
            node.next = prev
            # move all pointers forward
            prev = node
            node = temp
        return prev

        # time comp. = O(n), linked list grows based on input size
        # space comp. = O(1), vars 'prev', 'node' are constant
