class Solution:
    def __init__(self) -> None:
        self.stack = []

    def pop(self):
        item = self.stack.pop(-1)
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
            elif letter in ")}]":
                item = self.pop()
                if item != letter:
                    return False
        if len(self.stack) == 0:
            return True
        else:
            return False
                
            # elif letter == ")" and len(self.stack) > 0:
            #     item = self.pop()
            #     if item != ""
            # elif letter == "}" and len(self.stack) > 0:
            #     item = self.pop()
            # elif letter == "]" and len(self.stack) > 0:
            #     item = self.pop()
                
            else:
                return False
        if len(self.stack) != 0:
            return False
        else:
            return True


s = "){"
print(Solution().isValid(s))
