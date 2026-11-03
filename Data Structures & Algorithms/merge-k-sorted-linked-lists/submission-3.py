# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        from itertools import count
        counter = count()
        heap = []
        res = ListNode()
        dummy = res
        for ll in lists:
            if ll:
                heapq.heappush(heap, (ll.val, next(counter), ll))
        while heap:
            cur_node = heapq.heappop(heap)[2]

            res.next = cur_node
            res = res.next
            if cur_node.next:
                heapq.heappush(heap, (cur_node.next.val, next(counter), cur_node.next))
        return dummy.next


