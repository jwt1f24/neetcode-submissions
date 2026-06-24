# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode(0)
        l3 = list3
        l1 = list1
        l2 = list2

        # iterate through both lists, insert smaller nodes first
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
        
        # insert any extra nodes if either list finished iterating
        if l1:
            l3.next = l1
        else:
            l3.next = l2

        return list3.next # return the list but skip the first placeholder node

        # time comp. = O(n + m), both lists are iterated simultaneously
        # space comp. = O(1), vars: l1, l2, l3, are constant no matter input size
