# [Medium] Combination Sum

## Complexity
Time Complexity: O(N^(T/M + 1)), where N is the number of candidates, T is the target, and M is the minimum value among candidates. The maximum depth of the recursion tree is T/M, and at each node we can branch up to N times. Sorting takes O(N log N) which is dominated by the backtracking cost.
Space Complexity: O(T/M) to store the recursion stack and the temporary combination path.

## Explanation
This solution uses a backtracking approach with pruning to find all unique combinations. First, we sort the candidates array. Sorting allows us to stop exploring a branch early (prune) if the current candidate exceeds the remaining target, as any subsequent candidates will also be too large. During backtracking, we maintain the current remaining target and the path of chosen numbers. To allow the same number to be chosen multiple times but avoid duplicate combinations, we pass the current index 'i' to the next recursive call, preventing the algorithm from choosing elements that appear before 'i' in the sorted list.

## Solution
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        
        def backtrack(remain, combo, start):
            if remain == 0:
                results.append(list(combo))
                return
            
            for i in range(start, len(candidates)):
                # Since candidates are sorted, if the current candidate exceeds the remaining target,
                # then all subsequent candidates will also exceed it. We can safely break.
                if candidates[i] > remain:
                    break
                
                combo.append(candidates[i])
                # Recursively call backtrack with the same index 'i' to allow using the same number multiple times
                backtrack(remain - candidates[i], combo, i)
                combo.pop()
                
        backtrack(target, [], 0)
        return results
```
