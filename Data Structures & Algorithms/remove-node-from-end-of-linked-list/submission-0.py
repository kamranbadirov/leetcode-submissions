# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        crawler = head
        l = 0
        while crawler:
            l += 1
            crawler = crawler.next
        
        n = l - n

        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        i = 0
        while curr:
            if i == n:
              prev.next = curr.next
              break
            prev = curr
            curr = curr.next
            i += 1
        return dummy.next

        