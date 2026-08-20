# [Medium] Pow(x, n)

## Complexity
Time Complexity: O(log n) because the exponent n is halved in each iteration.
Space Complexity: O(1) auxiliary space as the solution only uses a few variables.

## Explanation
This solution uses iterative Binary Exponentiation (also known as exponentiation by squaring) to compute x^n in logarithmic time. If n is negative, we can transform the problem by replacing x with 1/x and n with -n. We then iterate while n > 0. If the least significant bit of n is 1 (i.e., n is odd), we multiply the result by the current power of x. In each step, we square x (x = x * x) and divide n by 2 (n >>= 1). This reduces the number of multiplications to O(log n).

## Solution
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1.0
        while n > 0:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans
```
