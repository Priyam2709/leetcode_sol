# [Medium] Longest Substring Without Repeating Characters

## Complexity
Time Complexity: O(N) where N is the length of the string, as we traverse the string exactly once. Space Complexity: O(min(N, M)) where M is the size of the character set (alphabet size, bounded by 128 for ASCII characters), since we store at most M unique characters in the hash map.

## Explanation
We use a sliding window approach with two pointers, `start` and `end`, and a hash map (`char_map`) to store the last seen index of each character. As we iterate through the string with `end`, we check if the character is already present in our current window. If it is, we shrink the window by moving the `start` pointer to the index right after the previous occurrence of that character. We then update the character's index in the map and compute the maximum window length found so far.

## Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        start = 0
        max_len = 0
        for end, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            char_map[char] = end
            max_len = max(max_len, end - start + 1)
        return max_len
```
