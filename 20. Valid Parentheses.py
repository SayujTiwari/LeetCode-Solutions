class Solution:
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        item = self.stack.pop()
        return item

    def push(self, item):
        self.stack.append(item)

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        for letter in s:
            print(self.stack)
            print(letter)
            if letter in "({[":
                self.push(letter)
            elif len(self.stack) > 0:
                if letter == ")" and self.stack[-1] == "(":
                    self.pop()
                if letter == "}" and self.stack[-1] == "{":
                    self.pop()
                if letter == "]" and self.stack[-1] == "[":
                    self.pop()
            else:
                return False
        if len(self.stack) == 0:
            return True
        else:
            return False


s = "()"
print(Solution().isValid(s))
