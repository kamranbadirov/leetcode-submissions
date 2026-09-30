# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        hold_it = None
        while head:
            hold_it = head.next
            head.next = tail
            tail = head
            head = hold_it
        return tail

        