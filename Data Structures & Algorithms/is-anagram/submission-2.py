from collections import Counter as counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = counter(s)
        count_t = counter(t)
        if len(count_s) != len(count_t):
            return False
        for k,v in count_t.items():
            if k not in count_s or count_s[k] != v:
                return False
        return True