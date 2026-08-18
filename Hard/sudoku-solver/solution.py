class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    digit = int(val)
                    mask = 1 << (digit - 1)
                    box = (r // 3) * 3 + (c // 3)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box] |= mask

        def backtrack(idx: int) -> bool:
            if idx == len(empty_cells):
                return True
            
            r, c = empty_cells[idx]
            box = (r // 3) * 3 + (c // 3)
            
            # Find available numbers (represented by 0s in the combined mask)
            allowed = ~(rows[r] | cols[c] | boxes[box]) & 0x1FF
            
            while allowed > 0:
                # Get the lowest set bit
                lsb = allowed & -allowed
                digit = lsb.bit_length()
                
                # Place the digit
                rows[r] |= lsb
                cols[c] |= lsb
                boxes[box] |= lsb
                board[r][c] = str(digit)
                
                if backtrack(idx + 1):
                    return True
                
                # Backtrack
                rows[r] &= ~lsb
                cols[c] &= ~lsb
                boxes[box] &= ~lsb
                
                # Clear the lowest set bit to try the next option
                allowed &= allowed - 1
                
            return False

        backtrack(0)