# [Hard] Sudoku Solver

## Complexity
Time Complexity: O(9^m) in the absolute worst-case, where m is the number of empty cells. Since the grid is fixed at 9x9, m <= 81. In practice, the search space is highly pruned by Sudoku constraints, running in less than 10-20ms.
Space Complexity: O(m) for the recursion stack and the list of empty cells. Since m <= 81, this simplifies to O(1) auxiliary space.

## Explanation
This solution uses backtracking optimized with bit manipulation. We maintain three arrays of integers (`rows`, `cols`, and `boxes`) representing bitmasks of used digits for each row, column, and 3x3 sub-grid. A set bit at position `d-1` indicates that the digit `d` is already used. During backtracking, we find all available numbers for a cell by performing a bitwise NOT on the union of the row, column, and box masks. We then iterate through each set bit in this 'allowed' mask using efficient bitwise operations (`lsb = allowed & -allowed` and `allowed &= allowed - 1`). Using `bit_length()` allows us to retrieve the actual digit in O(1) time. This minimizes overhead, avoids expensive set lookups, and yields an extremely fast Sudoku solver.

## Solution
```python
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
```
