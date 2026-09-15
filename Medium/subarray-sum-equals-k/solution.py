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