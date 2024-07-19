class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            test = numbers[start] + numbers[end]
            if test == target:
                return [start+1, end+1]
            elif test > target:
                end-=1
            else:
                start+=1
