class MinStack:

    def __init__(self):
        self.stack = []
        self.minValues = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minValues) == 0:
            self.minValues.append(val)
        elif self.minValues[len(self.minValues)-1] >= val:
            self.minValues.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minValues[len(self.minValues)-1]:
            self.minValues.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minValues[len(self.minValues)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()