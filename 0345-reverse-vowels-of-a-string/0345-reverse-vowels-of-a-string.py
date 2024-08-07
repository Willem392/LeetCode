class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
        
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if isVowel(s[l]) and isVowel(s[r]):
                tmp = s[r]
                s[r] = s[l]
                s[l] = tmp
                l += 1
                r -= 1
            else:
                if not isVowel(s[l]):
                    l += 1
                if not isVowel(s[r]):
                    r -= 1
        return ''.join(s)