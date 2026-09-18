class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ')':'(', ']':'['}

        for brac in s:
            if brac in {'(', '{', '['}:
                stack.append(brac)
            else:
                if stack and stack[-1] == pairs[brac]:
                    stack.pop()
                else:
                    return False
        return not stack
