# [Easy] Convert a Number to Hexadecimal

## Complexity
Time Complexity: O(1) because a 32-bit integer has at most 8 hexadecimal digits, so the loop runs a maximum of 8 times. Space Complexity: O(1) as the space used for the output array is at most 8 characters, which is constant.

## Explanation
To handle both positive and negative 32-bit integers, we first convert the number to its 32-bit unsigned equivalent using a bitwise AND operation with `0xffffffff`. This automatically handles the two's complement representation for negative numbers. We then extract the hexadecimal digits from right to left by repeatedly taking the remainder of the number modulo 16 (using bitwise `& 15`) and shifting the number right by 4 bits (using `>> 4`). Finally, we reverse the collected characters to get the correct order and return the string.

## Solution
```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Convert to 32-bit unsigned equivalent to handle two's complement for negatives
        num &= 0xffffffff
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            digit = num & 15  # Equivalent to num % 16
            result.append(hex_chars[digit])
            num >>= 4         # Equivalent to num //= 16
            
        return "".join(reversed(result))
```
