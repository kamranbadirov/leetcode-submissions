class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy_s = [c.lower() for c in s if c.isalnum()]
        return copy_s == copy_s[::-1]
        