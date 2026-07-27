# [Medium] Queue Reconstruction by Height

## Complexity
Time Complexity: O(N^2), where N is the number of people. Sorting takes O(N log N) time, and inserting N elements into a list at arbitrary indices takes O(N^2) in the worst case.
Space Complexity: O(N) to store the output queue.

## Explanation
The problem can be solved efficiently using a greedy approach by sorting. We sort the people primarily by height in descending order, and secondarily by their $k$-value in ascending order. When we process people in this sorted order, we insert each person into the output queue at the index equal to their $k$-value. Because we process taller people first, every person already in the queue is taller than or equal in height to the current person. Thus, inserting the current person at index $k$ guarantees that there are exactly $k$ taller or equal height people in front of them. Any subsequent insertions of shorter people will not affect the validity of the position of the taller people already placed.

## Solution
```python
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        # Sort people: 
        # 1. Primary key: height (h) in descending order (-x[0])
        # 2. Secondary key: k-value in ascending order (x[1])
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for p in people:
            # Since we process taller people first, the index where we insert 
            # a person is exactly their k-value. Any subsequent shorter person 
            # inserted will not affect the count of taller people in front.
            queue.insert(p[1], p)
            
        return queue
```
