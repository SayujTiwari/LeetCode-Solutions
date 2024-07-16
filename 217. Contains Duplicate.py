# checks to see if there is a duplicate integar in an array


# using hashmap
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False
