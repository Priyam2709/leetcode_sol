# [Medium] Permutations II

## Complexity
Time Complexity: O(N * N!) in the worst case (all unique elements), where N is the length of `nums`. Since N <= 8, this executes in less than 1 millisecond.
Space Complexity: O(N) auxiliary space for the recursion stack and the `used` array, excluding the memory required to store the final output list.

## Explanation
To generate unique permutations while handling duplicates, we first sort the input array `nums`. We use a backtracking approach with a helper array `used` to keep track of which elements are currently in our permutation path. To avoid duplicate permutations, we skip the current element if it is identical to the previous element (`nums[i] == nums[i-1]`) and the previous element hasn't been used in the current path (`not used[i-1]`). This constraint ensures that duplicate elements are always processed in a fixed relative order, thereby pruning redundant branches in the decision tree.

## Solution
```python
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                results.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates: if the current element is the same as the previous one,
                # we can only use it if the previous one has already been used in this path.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        nums.sort()
        results = []
        used = [False] * len(nums)
        backtrack([])
        return results
```
