# [Medium] Count and Say

## Complexity
Time Complexity: O(C^n) where C ≈ 1.303 (Conway's constant). The length of the string grows exponentially with rate C, and we perform a linear scan on each iteration. For the maximum constraint of n = 30, the length of the string is only 4,462 characters, which runs in less than a millisecond.
Space Complexity: O(C^n) to store the generated string of the n-th sequence in memory.

## Explanation
The solution iteratively computes the count-and-say sequence starting from the base case "1" up to the n-th element. For each step, we perform run-length encoding (RLE) on the current string. We traverse the string using a pointer, counting consecutive identical characters, and then append the count and the character itself to a list. Finally, we join the list to form the next string, repeating this process n - 1 times.

## Solution
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        for _ in range(1, n):
            next_str = []
            i = 0
            n_len = len(curr)
            while i < n_len:
                count = 1
                while i + 1 < n_len and curr[i] == curr[i+1]:
                    i += 1
                    count += 1
                next_str.append(str(count))
                next_str.append(curr[i])
                i += 1
            curr = "".join(next_str)
        return curr
```
