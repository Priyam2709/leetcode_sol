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