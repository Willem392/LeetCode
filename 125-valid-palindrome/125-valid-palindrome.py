class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                l.append(ch.lower())
        return l == l[::-1]