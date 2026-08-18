# [Medium] Combination Sum II

## Complexity
Time Complexity: O(2^N) in the worst case, where N is the number of candidates, as each element can either be chosen or not. However, sorting and aggressive pruning make the practical runtime significantly faster. Space Complexity: O(N) for the recursion stack depth and the path storage.

## Explanation
The problem is solved using a backtracking approach with sorting to handle duplicates efficiently. First, we sort the candidates list. Sorting serves two purposes: it allows us to break the loop early if a candidate exceeds the remaining target (pruning), and it groups identical elements together. During backtracking, we maintain a search index 'start' and only consider elements from this index onward to prevent duplicate combinations. If candidates[i] is identical to candidates[i-1] and i is greater than the current start index, we skip it because it would generate duplicate combination paths at the current decision level.

## Solution
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def backtrack(start: int, target: int, path: List[int]):
            if target == 0:
                results.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # If the current candidate is greater than the remaining target,
                # no subsequent elements can sum to the target because the list is sorted.
                if candidates[i] > target:
                    break
                
                # Skip duplicates to ensure uniqueness of combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return results
```
