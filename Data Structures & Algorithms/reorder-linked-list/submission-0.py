# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        mapping = {}

        dummy = head
        i = 0
        while dummy:
            mapping[i] = dummy
            i += 1
            dummy = dummy.next
        s, e = 0, len(mapping) -1 
        # print(mapping[0].next.val)
        while s < e:
            nxt = mapping[s].next
            mapping[s].next = mapping[e]
            mapping[e].next = nxt
            s += 1
            e -= 1
        mapping[s].next = None
