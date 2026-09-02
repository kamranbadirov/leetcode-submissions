class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        res = "4#neet"
        

        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #4#neet
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = j + 1 + length
            res.append(s[i:j])
            i = j
        return res


