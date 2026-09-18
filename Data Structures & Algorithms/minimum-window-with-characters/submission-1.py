from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        count = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(count)

        res, lenRes = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in count and window[c] == count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < lenRes:
                    lenRes = (r - l + 1)
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in count and count[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1] + 1] if lenRes < float('inf') else ""




        
        