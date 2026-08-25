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