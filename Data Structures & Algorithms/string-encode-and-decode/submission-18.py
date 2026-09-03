class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            l = len(s)
            res.append(str(l) + "#" + s)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        del_i = s.find("#")
        s_len = int(s[:del_i])
        res = []
        while del_i < len(s):
            start = del_i + 1
            end = start + s_len
            res.append(s[start:end])
            del_i = s.find("#", end)
            if del_i == -1:
                break
            s_len = int(s[end:del_i])
        return res


