class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = r = 0
        res = 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                res = max(res, r - l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                # move l until s[r] is removed

            seen.add(s[r])
            r += 1
        return max(res, r - l)



        