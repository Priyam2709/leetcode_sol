# [Hard] N-Queens

## Complexity
Time Complexity: O(N!) in the worst case, as we place at most one queen per row and column, and backtracking prune invalid branches early. For N = 9, the search space is extremely small.
Space Complexity: O(N) auxiliary space for the recursion stack and the state array storing queen positions.

## Explanation
This solution uses backtracking with bitwise operations to efficiently find all valid N-Queens configurations. We place queens row-by-row and use three bitmasks to track occupied columns (`cols`), left diagonals (`ld`), and right diagonals (`rd`). 

1. At each row, the bitwise OR `cols | ld | rd` represents all threatened columns.
2. Inverting this mask and taking the first `n` bits (`~(cols | ld | rd) & ((1 << n) - 1)`) gives the set of available columns where we can place a queen.
3. We iterate through each available position using `available_positions & -available_positions` to extract the lowest set bit efficiently.
4. When moving to the next row, we update our conflict masks. The left diagonal conflicts shift left (`<< 1`) and the right diagonal conflicts shift right (`>> 1`).
5. Once we successfully place `n` queens, we reconstruct the board from the state array and add it to the results.

## Solution
```python
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
```
