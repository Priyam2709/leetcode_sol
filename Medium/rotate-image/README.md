# [Medium] Rotate Image

## Complexity
Time Complexity: O(n^2), where n is the number of rows (or columns) in the matrix. Transposing takes O(n^2/2) operations and reversing each row takes O(n^2/2) operations, resulting in an overall time complexity of O(n^2).
Space Complexity: O(1) auxiliary space, as the modification is done completely in-place without allocating any additional matrices.

## Explanation
The algorithm rotates the matrix 90 degrees clockwise in-place using a two-step mathematical approach:
1. **Transpose the Matrix**: We iterate over the upper triangle of the matrix and swap `matrix[i][j]` with `matrix[j][i]`. This reflects the matrix over its main diagonal.
2. **Reverse Each Row**: After transposing, reversing the elements of each row yields the correct 90-degree clockwise rotation.

This approach is highly readable, easy to implement, and avoids complex coordinate mapping while maintaining optimal in-place performance.

## Solution
```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix (swap elements across the main diagonal)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
```
