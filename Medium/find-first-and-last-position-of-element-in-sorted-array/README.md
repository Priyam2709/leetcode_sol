# [Medium] Find First and Last Position of Element in Sorted Array

## Complexity
Time Complexity: $O(\log n)$ because we perform exactly two binary searches, each taking $O(\log n)$ time.\nSpace Complexity: $O(1)$ as we only use a few variables for pointers, requiring constant auxiliary space.

## Explanation
To achieve $O(\log n)$ runtime complexity, we can use binary search twice. Instead of writing two distinct binary search functions, we can write a single helper function `binary_search_left` that finds the index of the first element greater than or equal to a given target. We use this helper to find the first occurrence of the `target` (stored in `left_idx`). If the target is not found in the array (i.e., `left_idx` is out of bounds or `nums[left_idx] != target`), we return `[-1, -1]`. If it is found, we find the first index of `target + 1` and subtract `1` from it to get the last occurrence of the `target`. This keeps the code concise, elegant, and highly optimized.

## Solution
```python
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search_left(nums: list[int], target: int) -> int:
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low

        left_idx = binary_search_left(nums, target)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        # Find the insertion point for target + 1, and subtract 1 to get the last index of target
        right_idx = binary_search_left(nums, target + 1) - 1
        return [left_idx, right_idx]
```
