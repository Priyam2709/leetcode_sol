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