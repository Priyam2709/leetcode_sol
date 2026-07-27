# [Easy] Remove Duplicates from Sorted Array

## Complexity
Time Complexity: O(N), where N is the length of the array, since we perform a single pass over the elements. Space Complexity: O(1) auxiliary space, as the operation is done entirely in-place without using extra memory.

## Explanation
The solution uses a two-pointer approach. We maintain a `write_index` pointer to keep track of the position where the next unique element should be placed, and a `read_index` pointer to scan through the array. Since the array is sorted, any duplicate elements will be adjacent. We compare the current element at `read_index` with the last written unique element at `write_index - 1`. If they are different, we write the current element to `write_index` and increment it. This modifies the array in-place and keeps the unique elements in their relative order.

## Solution
```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
                
        return write_index
```
