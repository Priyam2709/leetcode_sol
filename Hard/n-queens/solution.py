class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        state = [0] * n
        
        def backtrack(r, cols, ld, rd):
            if r == n:
                board = []
                for val in state:
                    board.append('.' * val + 'Q' + '.' * (n - 1 - val))
                ans.append(board)
                return
            
            # Bitmask of all available positions for the current row
            # (cols | ld | rd) represents all threatened columns.
            # We invert it and mask to the first n bits.
            available_positions = ~(cols | ld | rd) & ((1 << n) - 1)
            
            while available_positions:
                # Get the lowest set bit (position of the queen)
                position = available_positions & -available_positions
                # Clear the lowest set bit
                available_positions ^= position
                
                col = position.bit_length() - 1
                state[r] = col
                
                # Recurse to the next row
                # ld (left diagonals) shifts left (increases index) for the next row
                # rd (right diagonals) shifts right (decreases index) for the next row
                backtrack(r + 1, cols | position, (ld | position) << 1, (rd | position) >> 1)
                
        backtrack(0, 0, 0, 0)
        return ans