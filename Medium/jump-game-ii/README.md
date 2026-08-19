# [Medium] Jump Game II

## Complexity
Time Complexity: O(n) because we iterate through the array of length n exactly once.
Space Complexity: O(1) as we only use a few variables to track indices and jumps.

## Explanation
This solution uses a greedy approach that is equivalent to a Breadth-First Search (BFS). We maintain three variables: 'jumps' (the minimum number of jumps needed so far), 'current_end' (the furthest index we can reach with the current number of jumps), and 'farthest' (the furthest index we can reach with one more jump). We iterate through the array up to 'n - 2'. At each index, we update 'farthest'. When we reach 'current_end', it means we must make another jump to proceed. Thus, we increment 'jumps' and update 'current_end' to 'farthest'. If 'current_end' reaches or exceeds the last index, we can stop early and return the number of jumps.

## Solution
```python
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
                    
        return jumps
```
