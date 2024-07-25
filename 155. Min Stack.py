class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.min.append(val)
        else:
            if val <= self.min[len(self.min) - 1]:
                self.min.append(val)

    def pop(self) -> None:
        if self.stack[len(self.stack) - 1] == self.min[len(self.min) - 1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min[len(self.min) - 1]
