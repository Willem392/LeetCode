class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        stackIndex = 0
        for ch in s:
            if ch == '*':
                stack.pop(stackIndex - 1)
                stackIndex -= 1
            else:
                stack.append(ch)
                stackIndex += 1
        ret = ""
        for ch in stack:
            ret += ch
        return ret