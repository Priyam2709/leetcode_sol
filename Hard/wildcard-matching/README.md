# [Hard] Wildcard Matching

## Complexity
Time Complexity: O(S * P) in the absolute worst case, but O(S + P) on average since backtracking is only triggered on mismatches after wildcards. Space Complexity: O(1) auxiliary space as we only use a few pointer variables.

## Explanation
This solution uses a highly optimized two-pointer approach with backtracking (greedy algorithm). We maintain pointers `s_ptr` and `p_ptr` for `s` and `p` respectively. When we encounter a `*`, we save its position (`star_idx`) and the current position in `s` (`s_tmp_idx`), then greedily assume `*` matches 0 characters by incrementing `p_ptr`. If we encounter a mismatch later, we backtrack to the last saved `*`, increment `s_tmp_idx` to let `*` match one more character, and reset our pointers to continue matching. After scanning `s`, we ensure any remaining characters in `p` are only `*` for a valid match.

## Solution
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        star_idx = -1
        s_tmp_idx = -1
        
        s_len, p_len = len(s), len(p)
        
        while s_ptr < s_len:
            # If characters match or pattern has '?'
            if p_ptr < p_len and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            # If pattern has '*', record the wildcard position and backtrack point
            elif p_ptr < p_len and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp_idx = s_ptr
                p_ptr += 1
            # If mismatch occurred but we have a active '*' wildcard
            elif star_idx != -1:
                # Backtrack: make the wildcard match one more character
                s_tmp_idx += 1
                s_ptr = s_tmp_idx
                p_ptr = star_idx + 1
            # Mismatch and no '*' wildcard to backtrack to
            else:
                return False
        
        # Ensure any remaining characters in pattern are '*'
        while p_ptr < p_len and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == p_len
```
