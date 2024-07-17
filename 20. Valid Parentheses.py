class Solution:
    # create Stack DS
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        item = self.stack.pop()
        return item

    def push(self, item):
        self.stack.append(item)

    # checking Function
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        for letter in s:
            if letter in "({[":
                self.push(letter)
            # checking each case
            elif len(self.stack) > 0:
                if letter == ")" and self.stack[-1] == "(":
                    self.pop()
                elif letter == "}" and self.stack[-1] == "{":
                    self.pop()
                elif letter == "]" and self.stack[-1] == "[":
                    self.pop()
                else:
                    return False
            else:
                return False
        if len(self.stack) == 0:
            return True
        else:
            return False
