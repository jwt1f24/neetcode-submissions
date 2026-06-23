# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head

        # continue iterating until there is no more nodes left in the list
        while node: 
            # reverse 2 pointers
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev