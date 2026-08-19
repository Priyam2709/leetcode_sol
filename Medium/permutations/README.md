# [Medium] Permutations

## Complexity
Time Complexity: O(N * N!) because there are N! permutations and copying each permutation takes O(N) time. Space Complexity: O(N) auxiliary space for the recursion call stack of depth N (excluding the space needed for the output).

## Explanation
This solution uses an in-place swap-based backtracking algorithm to generate all permutations. By swapping the element at the current index 'first' with each subsequent element (including itself), we generate all possible choices for the current position. After exploring down the recursion tree, we swap back (backtrack) to restore the list to its original state for the next branch. When the index 'first' reaches the end of the array, a copy of the current configuration is added to the result.

## Solution
```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        
        def backtrack(first: int):
            if first == n:
                res.append(nums[:])
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        backtrack(0)
        return res
```
