# [Easy] Length of Last Word

## Complexity
Time Complexity: O(N) in the worst case, where N is the length of the string, since we traverse the string at most once.
Space Complexity: O(1) auxiliary space, as we only use a pointer and a counter variable.

## Explanation
To solve the problem with optimal space efficiency, we traverse the string from right to left. First, we skip any trailing space characters to position our pointer at the end of the last word. Then, we count the number of non-space characters until we either hit another space or reach the beginning of the string. This count is the length of the last word.

## Solution
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip any trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # Count the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length
```
