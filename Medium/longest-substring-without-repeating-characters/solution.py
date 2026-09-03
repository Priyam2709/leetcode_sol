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