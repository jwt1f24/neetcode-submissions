# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # iterate by checking if fast node exists
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            # index and nodes match, cycle exists
            if slow == fast:
                return True
                
        return False

        # time comp. = O(n), linked list grows based on input size
        # space comp. = O(1), var 'fast' & 'slow' are constant no matter input size
