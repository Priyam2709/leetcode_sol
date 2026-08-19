# [Medium] Multiply Strings

## Complexity
Time Complexity: O(M * N) where M and N are the lengths of `num1` and `num2` respectively, because we compute the product of every pair of digits. 
Space Complexity: O(M + N) to store the result array which can have at most M + N digits.

## Explanation
The solution simulates the standard grade-school multiplication algorithm. We represent the result in an array `res` of size `len(num1) + len(num2)`. We iterate through both strings from right to left. For each pair of digits `num1[i]` and `num2[j]`, their product is placed at indices `i + j` and `i + j + 1` in the result array. Specifically, the units place of the product (plus any existing value/carry) goes to `i + j + 1`, and the tens place carry is added to `i + j`. After computing all products, we skip any leading zeros and construct the final result string.

## Solution
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        # Multiply from right to left
        for i in range(m - 1, -1, -1):
            n1 = ord(num1[i]) - 48  # ord('0') is 48
            for j in range(n - 1, -1, -1):
                n2 = ord(num2[j]) - 48
                mul = n1 * n2
                
                # Indices in the result array for placing the product
                p1, p2 = i + j, i + j + 1
                
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Find the first non-zero element
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        return "".join(map(str, res[start:]))
```
