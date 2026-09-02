class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s))+'#' + s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        res = []
        while i < len(s):
            size = ""
            while s[i] != '#':
                size += s[i]
                i += 1
            i += 1
            res.append(s[i:i+int(size)])
            i += int(size)
        return res