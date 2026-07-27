# [Medium] Divide Two Integers

## Complexity
Time Complexity: O(1) because the loop always runs exactly 32 times (from 31 down to 0), regardless of the input size.
Space Complexity: O(1) as we only use a few variables to store the state.

## Explanation
The algorithm uses bit manipulation to perform division in O(log N) time, avoiding multiplication, division, and modulo operations. We find the quotient by representing it as a sum of powers of 2. We iterate from the 31st bit down to the 0th bit. For each bit position `i`, we check if `b << i` can fit into `a`. To prevent overflow issues in a strict 32-bit integer environment, we check `(a >> i) >= b` instead of `a >= (b << i)`. If it fits, we subtract `b << i` from `a` and add `1 << i` to our quotient. Finally, we apply the proper sign and clamp the result within the 32-bit signed integer range.

## Solution
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle the overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        
        res = 0
        # Iterate from the largest power of 2 down to 0
        for i in range(31, -1, -1):
            # To prevent overflow during bit shifting, we use right shift on 'a'
            # instead of left shift on 'b'. (a >> i) >= b is equivalent to a >= (b << i)
            if (a >> i) >= b:
                a -= b << i
                res += 1 << i
                
        # Apply the sign and clamp the result to 32-bit signed integer range
        res = -res if negative else res
        return max(INT_MIN, min(INT_MAX, res))
```
