# [Hard] Longest Valid Parentheses

## Complexity
Time Complexity: $O(n)$ where $n$ is the length of the string, as we make exactly two passes over the string.
Space Complexity: $O(1)$ auxiliary space, since we only use a few integer variables.

## Explanation
This solution uses a two-pass greedy scanning algorithm. We maintain two counters, 'left' and 'right', representing the number of open and close parentheses respectively.

1. In the first pass (left-to-right), we increment the counters accordingly. Whenever 'left' equals 'right', we have a valid substring and update our maximum length. If 'right' exceeds 'left', it means the current substring is invalid, so we reset both counters to 0.
2. This single pass can miss cases where there are more open parentheses than close ones (e.g., '(()'). To handle this, we perform a second pass from right-to-left. In this pass, we reset the counters to 0 when 'left' exceeds 'right'.

Combining both passes ensures we find the longest valid parentheses substring in $O(1)$ extra space.

## Solution
```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        
        # Left-to-right pass
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
                
        left = right = 0
        # Right-to-left pass
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
                
        return max_len
```
