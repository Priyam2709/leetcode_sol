# [Easy] Convert a Number to Hexadecimal

## Complexity
Time Complexity: O(1) because a 32-bit integer has at most 8 hexadecimal digits, so the loop runs at most 8 times. Space Complexity: O(1) auxiliary space as the output string and array store at most 8 characters.

## Explanation
To represent both positive and negative 32-bit integers, we first convert the input into its 32-bit unsigned integer equivalent using `num & 0xffffffff`. This naturally handles negative numbers using two's complement. Then, we repeatedly take the least significant 4 bits (using `num & 15`) to find the corresponding hexadecimal character from a predefined map, and shift the number right by 4 bits (`num >>= 4`). We collect these characters and reverse them to form the final hexadecimal string. If the input is 0, we return '0' immediately.

## Solution
```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Convert to a 32-bit unsigned integer to handle two's complement for negatives
        num &= 0xffffffff
        
        hex_map = "0123456789abcdef"
        result = []
        
        while num > 0:
            digit = num & 15  # Equivalent to num % 16
            result.append(hex_map[digit])
            num >>= 4         # Equivalent to num // 16
            
        return "".join(reversed(result))
```
