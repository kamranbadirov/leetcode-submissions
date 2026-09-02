class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        num_count = Counter(nums)
        max_heap = []
        for num, count in num_count.items():
            heapq.heappush(max_heap,(-count, num))
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
