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