class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(0, len(s)):
            curString = ""
            for j in range(i, len(s)):
                if s[j] in curString:
                    break
                else:
                    curString += s[j]
                    if longest < len(curString):
                        longest = len(curString)
        return longest
                    
                
            
        