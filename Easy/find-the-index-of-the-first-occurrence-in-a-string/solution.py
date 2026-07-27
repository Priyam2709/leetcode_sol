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