class Solution:
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        self.stack.pop(-1)

    def push(self, item):
        self.stack.append(item)

    def isValid(self, s: str) -> bool:
        for letter in s:
            if letter == "(" or letter == "{" or letter == "[":
                self.push(s)
            else:
                self.pop()
        if len(self.stack) == 0:
            return True
        else:
            return False


s = "()"
print(Solution().isValid(s))
