class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            digits = [x for x in row if x!= "."]
            if len(digits) != len(set(digits)):
                return False
        
        for col in zip(*board):
            digits = [x for x in col if x!= "."]
            if len(digits) != len(set(digits)):
                return False

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                box = [board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]

                digits = [x for x in box if x != "."]
                if len(digits) != len(set(digits)):
                    return False
        return True
