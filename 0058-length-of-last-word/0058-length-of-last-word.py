class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(s.split(" "))
        res = []
        for i in l:
            if i != '':
                res.append(i)
        return(len(res[-1]))