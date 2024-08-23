class Solution:
    def removeStars(self, s: str) -> str:
        while '*' in s:
            index = s.index('*')
            s = s[:index - 1] + s[index + 1:]
        return s