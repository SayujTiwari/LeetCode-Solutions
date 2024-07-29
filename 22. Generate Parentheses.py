class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        days_list = []
        x = 0
        while True:
            for i in range(len(temperatures)):
                temp = temperatures[x]
                # print(f"The current temp: {temp}")
                if i == len(temperatures) - 1:
                    days_list.append(0)
                elif temp < temperatures[i + 1]:
                    stack.append(temperatures[i + 1])
                    # print(f"The stack: {stack}")
                    days_list.append(len(stack))
                    stack = []
                    # print(f"X is: {x}")
                    x += 1
                else:
                    stack.append(temperatures[i + 1])
                    # print(f"The stack: {stack}")
            if x == len(temperatures) - 1:
                # break
                return days_list


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution.dailyTemperatures(temperatures, temperatures))
