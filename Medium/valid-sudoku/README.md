# [Medium] Valid Sudoku

## Complexity
Time Complexity: O(1) since the board is always of fixed size 9x9, requiring a constant 81 operations. Space Complexity: O(1) because the auxiliary space required for the hash sets is bounded by the fixed board size.

## Explanation
The solution uses hash sets to keep track of the numbers encountered so far in each row, column, and 3x3 sub-box. We iterate through each cell in the 9x9 board. If a cell contains a digit, we map its coordinates to its corresponding row, column, and box index. The box index is calculated using the formula `(row // 3) * 3 + (col // 3)`. If the digit is already present in the set for its row, column, or box, the board is invalid and we return False. If we successfully traverse the entire board without any conflicts, we return True.

## Solution
```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                box_idx = (r // 3) * 3 + (c // 3)
                
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
```
