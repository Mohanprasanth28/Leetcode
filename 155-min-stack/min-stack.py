class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append(val)
        else:
            if val >= self.min_val:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.min_val)
                self.min_val = val
        

    def pop(self) -> None:
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.min_val:
            self.min_val = 2 * self.min_val - top
        

    def top(self) -> int:
        if not self.stack:
            return None
        top = self.stack[-1]
        return top if top >= self.min_val else self.min_val

    def getMin(self) -> int:
       return self.min_val if self.stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()