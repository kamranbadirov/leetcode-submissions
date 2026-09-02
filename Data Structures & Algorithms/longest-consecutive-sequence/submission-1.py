class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for n in nums:
            cur_len = 1
            if n - 1 in num_set:
                continue
            cur_len = 1
            cur_seq = n
            while cur_seq + 1 in num_set:
                cur_len += 1
                cur_seq += 1
            res = max(res, cur_len)
        return res
            
