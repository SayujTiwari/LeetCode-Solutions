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
                self.push(letter)
            elif letter == ")" and self.stack[-1] == "(":
                self.pop()
            elif letter == "}" and self.stack[-1] == "{":
                self.pop()
            elif letter == "]" and self.stack[-1] == "[":
                self.pop()
            else:
                return False
        return True


s = "({})[}()"
print(Solution().isValid(s))
