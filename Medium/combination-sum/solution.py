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