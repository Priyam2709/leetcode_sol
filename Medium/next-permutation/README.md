# [Medium] Next Permutation

## Complexity
Time Complexity: O(N) because we make at most three passes over the array of size N (one to find i, one to find j, and one to reverse the suffix). Space Complexity: O(1) auxiliary space as the modification is done completely in-place.

## Explanation
The algorithm finds the next lexicographically greater permutation in-place through a single pass. First, it scans from right to left to find the first element 'nums[i]' that is smaller than its successor 'nums[i+1]'. If no such element is found, the array is in descending order (the last permutation), so we reverse the entire array to get the smallest permutation. Otherwise, we scan from right to left again to find the first element 'nums[j]' that is strictly greater than 'nums[i]'. We swap 'nums[i]' and 'nums[j]', and then reverse the suffix starting at 'i + 1' to restore the sorted ascending order of the remaining part, achieving the next lexicographical permutation.

## Solution
```python
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to its right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap them
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting at i + 1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```
