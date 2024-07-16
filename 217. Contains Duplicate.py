# checks to see if there is a duplicate integar in an array


# using dictionary
class Solution:
    # makes it so you only have to iterate through array one time to check
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:  # checking if it is in dictionary
                return True
            seen[num] = (
                seen.get(num, 0) + 1
            )  # adding a count to keep track of how many times it has come up
        return False
