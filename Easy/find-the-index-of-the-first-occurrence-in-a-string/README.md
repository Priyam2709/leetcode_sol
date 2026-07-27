# [Easy] Find the Index of the First Occurrence in a String

## Complexity
Time Complexity: O(N + M) where N is the length of `haystack` and M is the length of `needle`. Building the LPS array takes O(M) time, and the matching process takes O(N) time.
Space Complexity: O(M) to store the LPS array.

## Explanation
This solution implements the Knuth-Morris-Pratt (KMP) string matching algorithm. KMP avoids unnecessary comparisons by precomputing a Longest Proper Prefix which is also a Suffix (LPS) table for the 'needle'. The LPS array allows the search pointer to backtrack in the pattern ('needle') rather than resetting the 'haystack' pointer to the beginning of the mismatch, guaranteeing linear time complexity.

## Solution
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
            
        # Build LPS (Longest Proper Prefix which is also Suffix) array
        lps = [0] * m
        prev_lps = 0
        i = 1
        while i < m:
            if needle[i] == needle[prev_lps]:
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            else:
                if prev_lps != 0:
                    prev_lps = lps[prev_lps - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        # Search matching pattern
        i = 0  # index for haystack
        j = 0  # index for needle
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == m:
                return i - j
            elif i < n and haystack[i] != needle[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
```
