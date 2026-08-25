# [Medium] Unique Paths

## Complexity
Time Complexity: O(min(m, n)) to compute the binomial coefficient.
Space Complexity: O(1) auxiliary space.

## Explanation
To reach the bottom-right corner of an m x n grid from the top-left corner, the robot must make exactly m - 1 downward moves and n - 1 rightward moves. The total number of moves is (m - 1) + (n - 1) = m + n - 2. The number of unique paths is the number of ways to choose which of these moves are down moves, which is given by the binomial coefficient C(m + n - 2, m - 1). We can compute this directly and efficiently using Python's built-in `math.comb` function.

## Solution
```python
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)
```
