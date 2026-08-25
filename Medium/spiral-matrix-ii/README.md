# [Medium] Spiral Matrix II

## Complexity
Time Complexity: O(n^2) because we visit and update each of the n^2 cells exactly once. Space Complexity: O(1) auxiliary space, as we do not use any extra data structures beyond the output matrix of size O(n^2).

## Explanation
We can generate the spiral matrix by simulating the movement layer-by-layer. We initialize an n x n matrix with zeros and track our position (r, c) starting at (0, 0) and our current direction with an index variable. The directions are ordered as right, down, left, and up. In each step, we write the current value into the matrix and calculate the next candidate position. If the candidate position is out of bounds or already contains a non-zero value, we turn 90 degrees clockwise by changing our direction index. We repeat this process for all numbers from 1 to n^2.

## Solution
```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        r, c, di = 0, 0, 0
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        for val in range(1, n * n + 1):
            matrix[r][c] = val
            nr, nc = r + dr[di], c + dc[di]
            if not (0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0):
                di = (di + 1) % 4
            r += dr[di]
            c += dc[di]
            
        return matrix
```
