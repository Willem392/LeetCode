class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = []
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                l.append(ch)
        return l == l[::-1]