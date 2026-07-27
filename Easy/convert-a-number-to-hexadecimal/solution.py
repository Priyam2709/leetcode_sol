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