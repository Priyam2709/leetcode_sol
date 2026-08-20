class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        limit = (1 << n) - 1
        
        def backtrack(cols: int, ld: int, rd: int):
            if cols == limit:
                self.count += 1
                return
            
            # Identify all open positions in the current row
            # (cols | ld | rd) gives all threatened columns
            # ~ invert flips them to represent free positions, & limit keeps it within n bits
            poss = ~(cols | ld | rd) & limit
            
            while poss:
                # Get the lowest set bit (rightmost available column)
                curr = poss & -poss
                poss -= curr
                # Recurse for the next row
                # cols | curr: mark column as occupied
                # (ld | curr) << 1: shift left diagonal conflicts leftward for the next row
                # (rd | curr) >> 1: shift right diagonal conflicts rightward for the next row
                backtrack(cols | curr, (ld | curr) << 1, (rd | curr) >> 1)
                
        backtrack(0, 0, 0)
        return self.count