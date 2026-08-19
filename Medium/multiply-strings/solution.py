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