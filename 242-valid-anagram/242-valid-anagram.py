class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS, charT = list(s), list(t)
        charS.sort()
        charT.sort()
        return False if charS != charT else True