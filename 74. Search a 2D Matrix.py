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
