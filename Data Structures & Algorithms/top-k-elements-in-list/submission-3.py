import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-k,v) for v,k in count.items()]
        heapq.heapify(heap)
        res = []
        while k:
            v, k_ = heapq.heappop(heap)
            res.append(k_)
            k -= 1
        return res
        