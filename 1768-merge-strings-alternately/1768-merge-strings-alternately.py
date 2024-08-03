class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longer = max(len(word1), len(word2))
        res = ''
        for i in range(longer):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res