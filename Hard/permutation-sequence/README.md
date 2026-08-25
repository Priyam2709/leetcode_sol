# [Hard] Permutation Sequence

## Complexity
Time Complexity: O(n^2). There are $n$ iterations, and in each iteration, we perform a list deletion (pop) which takes $O(n)$ time. Since $n \le 9$, this runs almost instantaneously.
Space Complexity: O(n) to store the list of digits and the generated result.

## Explanation
The problem can be solved efficiently by mapping the $k$-th permutation directly using factorials (factorial number system / Cantor expansion). For a permutation of size $n$, the first digit partitions the total $n!$ permutations into $n$ groups of size $(n-1)!$ each. By converting $k$ to a 0-based index and dividing it by $(n-1)!$, we can determine the exact index of the digit that must go first from our list of remaining digits. We then remove this digit from the pool, update $k$ to the remainder, and repeat the process for the remaining positions down to $0!$.

## Solution
```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        # Precompute factorials for division
        factorials = [1] * (n + 1)
        for i in range(1, n + 1):
            factorials[i] = factorials[i-1] * i
            
        # List of available digits
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Convert k to 0-based indexing
        k -= 1
        
        result = []
        for i in range(n - 1, -1, -1):
            # Determine the index of the next digit
            idx = k // factorials[i]
            result.append(numbers[idx])
            # Remove selected digit to avoid repetition
            numbers.pop(idx)
            # Update k for the next iteration
            k %= factorials[i]
            
        return "".join(result)
```
