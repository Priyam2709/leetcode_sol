# [Easy] Search Insert Position

## Complexity
Time Complexity: O(log n) because the search space is halved at each step of the binary search.
Space Complexity: O(1) as we only use a constant amount of extra space for the pointers.

## Explanation
This problem can be efficiently solved using binary search because the input array is already sorted. We maintain two pointers, `left` and `right`, representing the current search boundaries. In each step, we calculate the middle index `mid`. If `nums[mid]` equals the target, we return `mid`. If `nums[mid]` is less than the target, the target must be in the right half, so we update `left = mid + 1`. Otherwise, the target is in the left half, so we update `right = mid - 1`. If the target is not found, the loop terminates when `left > right`, at which point `left` correctly points to the index where the target should be inserted to maintain order.

## Solution
```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
```
