class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search_left(nums: list[int], target: int) -> int:
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low

        left_idx = binary_search_left(nums, target)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        # Find the insertion point for target + 1, and subtract 1 to get the last index of target
        right_idx = binary_search_left(nums, target + 1) - 1
        return [left_idx, right_idx]