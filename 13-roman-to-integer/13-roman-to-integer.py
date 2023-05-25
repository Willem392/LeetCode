class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        i = 0
        while i < len(s):
            if s[i] == 'M':
                output += 1000
            elif s[i] == 'D':
                output += 500
            elif s[i] == 'C':
                if i + 1 < len(s):
                    if s[i+1] == 'D':
                        output += 400
                        i += 1
                    elif s[i+1] == 'M':
                        output += 900
                        i += 1
                    else:
                        output += 100
                else:
                    output += 100
            elif s[i] == 'L':
                output += 50
            elif s[i] == 'X':
                if i + 1 < len(s):
                    if s[i+1] == 'L':
                        output += 40
                        i += 1
                    elif s[i+1] == 'C':
                        output += 90
                        i += 1
                    else:
                        output += 10
                else:
                    output += 10
            elif s[i] == 'V':
                output += 5
            elif s[i] == 'I':
                if i + 1 < len(s):
                    if s[i+1] == 'V':
                        output += 4
                        i += 1
                    elif s[i+1] == 'X':
                        output += 9
                        i += 1
                    else:
                        output += 1
                else:
                    output += 1
            i += 1
        return output