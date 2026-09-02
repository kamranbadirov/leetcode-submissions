class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0 
        res = 0
        counter = defaultdict(int)
        i = j = 0

        while j < len(s):
            if s[j] in counter:
                res = max(res, longest)

                while counter[s[j]] > 0 and i <= j:
                    counter[s[i]] -= 1
                    i += 1
                    longest -= 1
            counter[s[j]] += 1
            j += 1
            longest += 1
        return max(res, longest)

        