class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t != '+' and t != '-' and t != '*' and t != '/':
                stack.append(int(t))
            else:
                n = stack.pop()
                m = stack.pop()
                if t == '+':
                    stack.append(int(m+n))
                elif t == '*':
                    stack.append(int(m*n))
                elif t == '-':
                    stack.append(int(m-n))
                elif t == '/':
                    stack.append(int(m/n))
        return stack.pop()