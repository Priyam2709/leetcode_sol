# [Medium] Search in Rotated Sorted Array

## Complexity
Time Complexity: O(log n) since we divide the search space in half at each step of the binary search.
Space Complexity: O(1) as we only use a few variables for pointers, requiring no extra memory.

## Explanation
The problem asks us to search for a target value in a rotated sorted array of unique integers. A standard binary search can be adapted here. In any rotation of a sorted array, at least one of the two halves (left or right) after splitting at the midpoint is guaranteed to be sorted. 

We calculate the midpoint `mid`. If `nums[mid]` is the target, we return its index. If not, we determine which half is sorted:
1. If `nums[low] <= nums[mid]`, the left half is sorted. We then check if the target lies within the range of this sorted left half. If it does, we narrow our search to the left half (`high = mid - 1`); otherwise, we search the right half (`low = mid + 1`).
2. Otherwise, the right half must be sorted. We check if the target lies within the range of this sorted right half. If it does, we search the right half (`low = mid + 1`); otherwise, we search the left half (`high = mid - 1`).

If the element is not found when `low > high`, we return `-1`.

## Solution
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if the target lies within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if the target lies within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1
```
