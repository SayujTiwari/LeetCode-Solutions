class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = start + ((end - start) // 2)
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
print(Solution.search(nums, nums, 5))
