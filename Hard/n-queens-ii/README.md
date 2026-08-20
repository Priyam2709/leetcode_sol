# [Hard] N-Queens II

## Complexity
Time Complexity: O(N!) in the worst case, as we explore permutations of queen placements. However, due to pruning and extremely fast bitwise operations, it runs in a fraction of a millisecond for N <= 9.
Space Complexity: O(N) auxiliary space representing the recursion stack depth.

## Explanation
This solution uses highly optimized bitwise backtracking to solve the N-Queens problem. We represent the occupancy of columns, left diagonals (ld), and right diagonals (rd) as bitmasks. For any row, the bitwise OR of these three masks represents all under-attack positions. By inverting this mask (~), we find the safe positions. We recursively place a queen in each safe position, update the bitmasks (shifting the left diagonal mask left and the right diagonal mask right to reflect the movement down to the next row), and backtrack. This approach avoids auxiliary arrays or sets, making it extremely fast with very low overhead.

## Solution
```python
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
```
