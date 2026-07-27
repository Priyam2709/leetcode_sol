# [Easy] Remove Element

## Complexity
Time Complexity: O(N), where N is the length of the array `nums`, because we traverse the array exactly once.
Space Complexity: O(1), as the modification is done in-place without using any extra memory.

## Explanation
The solution uses a two-pointer approach to modify the array in-place. We maintain a pointer `write_index` that tracks the position where the next non-`val` element should be placed. We iterate through the array with a reader pointer `i`. Whenever `nums[i]` is not equal to `val`, we copy its value to `nums[write_index]` and increment `write_index`. This shifts all elements that are not equal to `val` to the front of the array. Finally, `write_index` will represent the number of elements not equal to `val` (which is `k`), and we return this value.

## Solution
```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
```
