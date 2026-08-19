# [Unknown] First Missing Positive

## Complexity
Time Complexity: O(n). Although there is a nested while loop, each swap places at least one number in its correct final position. Since a number is never moved once it is in its correct position, there are at most n swaps in total across the entire run. Space Complexity: O(1) as the sorting is done in-place with no extra memory.

## Explanation
The algorithm uses a cyclic sort approach to place each number in its correct position. Specifically, any integer `x` in the range `[1, n]` (where `n` is the size of the array) should ideally be placed at index `x - 1`. We iterate through the array, and for each element, while it is in the range `[1, n]` and not at its correct index, we swap it with the element at its target index. This process places at least one number in its correct position with each swap. After rearranging, we iterate through the array to find the first index `i` where `nums[i] != i + 1`, which indicates that `i + 1` is the first missing positive. If all positions are correct, the missing number is `n + 1`.

## Solution
```python
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
```
