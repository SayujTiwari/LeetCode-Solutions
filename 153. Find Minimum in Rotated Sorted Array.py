class Solution:
    # check one half and then the other bc there are two subarrays that are sorted, and check both sides to find the minimum
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums) - 1
        minNum = float("inf")
        while start <= end:
            middle = start + ((end - start) // 2)
            if nums[start] <= nums[middle]:
                minNum = min(minNum, nums[start])
                start = middle + 1
            else:
                minNum = min(minNum, nums[middle])
                end = middle - 1
        return minNum
