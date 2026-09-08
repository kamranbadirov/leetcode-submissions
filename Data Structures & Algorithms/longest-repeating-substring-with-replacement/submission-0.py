class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        most_freq = 0
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            most_freq = max(most_freq, count[s[right]])

            while (right - left + 1) - most_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res




        