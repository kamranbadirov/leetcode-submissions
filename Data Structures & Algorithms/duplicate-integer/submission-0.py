class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        for i,k in num_count.items():
            if k > 1:
                return True
        return False
        