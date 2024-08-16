class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tmp = ''
        res = []
        for c in s:
            if c != ' ':
                tmp += c
            elif tmp != '':
                res.append(tmp)
                tmp = ''
        if tmp != '':
                res.append(tmp)
                tmp = ''
        return len(res[-1])
        
        '''
        l = list(s.split(" "))
        res = []
        for i in l:
            if i != '':
                res.append(i)
        return(len(res[-1]))
        '''