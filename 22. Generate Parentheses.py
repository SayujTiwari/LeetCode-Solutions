class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n  # makes sure its in the correct index by adding placeholders.
        stack = []  # this will store the indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop the index from the stack
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            # Push the current index onto the stack
            stack.append(i)

        return answer
