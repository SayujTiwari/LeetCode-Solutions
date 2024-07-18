class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)  # create an answer array

        prefix = 1  # prefix of first one has to be one
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1  # the postfix on the last value will be
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer  # used same array to save pre to save memory


nums = [1, 2, 3, 4]

print(Solution().productExceptSelf(nums))
