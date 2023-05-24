class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        palindrone = ""
        for i in range (0, len(s)):
            curString = ""
            for j in range(i, len(s)):
                curString += s[j]
                if curString == curString[::-1] and len(curString) > longest:
                    longest = len(curString)
                    palindrone = curString
        return palindrone
        