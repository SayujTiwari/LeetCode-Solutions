class Solution:

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = ["*", "+", "-", "/"]
        for token in tokens:
            if token in ops:
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                if token == "+":
                    stack.append(int(value1 + value2))
                elif token == "-":
                    stack.append(int(value1 - value2))
                elif token == "*":
                    stack.append(int(value1 * value2))
                elif token == "/":
                    stack.append(int(value1 / value2))
            else:
                stack.append(token)
        return int(stack[0])
