class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowMap = {}
        colMap = {}
        squareMap = {}
        for row in board:
            for col in row:
                if colMap.get(col) == 1:
                    return False
                else:
                    colMap[col] = 1


"""
Create a way to select the 3x3 square, each of them

"""
