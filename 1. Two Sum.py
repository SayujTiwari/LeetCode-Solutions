class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        # O(n) Time
        for i in range(len(nums)):
            difference = target - nums[i]
            # if the difference is in the hashMap it means that those two integars are the two sum
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[nums[i]] = i
