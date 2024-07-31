class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            middle = start + ((end - start) // 2)
            if target in matrix[middle]:
                return True
            elif target < matrix[middle][0]:
                end = middle - 1
            else:
                start = middle + 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
print(Solution.searchMatrix(matrix, matrix, 3))
