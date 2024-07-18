"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[0])
            else:
                prefix.append(nums[i] * prefix[i - 1])
        for i in range(-1, -len(nums) - 1, -1):
            if i == -1:
                postfix.append(nums[i])
            else:
                postfix.insert(i - 1, postfix[i + 1] * nums[i])
        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(1 * postfix[i + 1])
            elif i == len(nums) - 1:
                answer.append(1 * prefix[i - 1])
            else:
                answer.append(prefix[i - 1] * postfix[i + 1])
        return answer


"""

"""

nums = [1, 2, 3, 4]

print(Solution().productExceptSelf(nums))
