class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        for word in s.split()[::-1]:
            res += word + " "
        return res[:-1]