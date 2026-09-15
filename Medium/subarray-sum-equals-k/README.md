# [Medium] Subarray Sum Equals K

## Complexity
Time Complexity: O(N) where N is the length of the array, since we traverse the array exactly once and perform O(1) average-time dictionary lookups and insertions.
Space Complexity: O(N) to store the prefix sums in the hash map in the worst case when all prefix sums are unique.

## Explanation
The problem can be efficiently solved using a prefix sum approach combined with a hash map. Let the prefix sum up to index $j$ be $P[j]$. The sum of any subarray from index $i$ to $j$ is given by $P[j] - P[i-1]$. We want to find the number of pairs $(i, j)$ such that $P[j] - P[i-1] = k$, which can be rearranged to $P[i-1] = P[j] - k$. By iterating through the array and keeping track of the prefix sum frequencies in a hash map, we can check in $O(1)$ time if there exists a previous prefix sum equal to $curr\_sum - k$ and add its count to our answer. We initialize the hash map with `{0: 1}` to account for subarrays starting at index 0.

## Solution
```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sums = {0: 1}
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefix_sums:
                count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            
        return count
```
