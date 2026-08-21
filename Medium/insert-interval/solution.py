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