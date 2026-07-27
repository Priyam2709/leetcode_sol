# [Easy] Convert a Number to Hexadecimal

## Complexity
Time Complexity: O(1) because a 32-bit integer has a maximum of 8 hexadecimal digits, meaning the loop runs at most 8 times.
Space Complexity: O(1) auxiliary space, as the size of the output string is at most 8 characters.

## Explanation
To convert the 32-bit integer to hexadecimal, we first convert the number to its 32-bit unsigned representation using a bitwise AND with `0xffffffff`. This naturally handles negative numbers using two's complement. We then repeatedly extract the last 4 bits of the number (using `num & 0xf`) to find the corresponding hexadecimal character from a lookup string, and right-shift the number by 4 bits (`num >>= 4`). We repeat this until the number becomes 0, and then return the reversed character sequence as the final string.

## Solution
```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Convert to 32-bit unsigned integer to handle negative numbers via two's complement
        num = num & 0xffffffff
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            digit = num & 0xf
            result.append(hex_chars[digit])
            num >>= 4
            
        return "".join(reversed(result))
```
