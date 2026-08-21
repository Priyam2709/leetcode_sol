# [Medium] Insert Interval

## Complexity
Time Complexity: O(N) where N is the number of intervals, as we iterate through the list of intervals exactly once. Space Complexity: O(N) to store the output list. The auxiliary space complexity is O(1) if we exclude the memory needed for the output.

## Explanation
The algorithm processes the sorted intervals in a single pass of three stages: 1. Add all existing intervals that finish before the new interval starts. 2. Merge all overlapping intervals with the new interval by progressively updating its start to the minimum start of overlapping intervals, and its end to the maximum end of overlapping intervals. 3. Append the merged interval, and then add all remaining intervals that start after the merged interval ends. This avoids sorting again and guarantees the correct linear scan order.

## Solution
```python
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        new_start, new_end = newInterval
        
        # Step 1: Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1
            
        # Step 2: Merge all overlapping intervals into the new interval
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        result.append([new_start, new_end])
        
        # Step 3: Add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result
```
