# [Medium] Queue Reconstruction by Height

## Complexity
Time Complexity: O(N^2), where N is the number of people. Sorting takes O(N log N) time, and inserting each of the N elements into the list takes O(N) time in the worst case.
Space Complexity: O(N) to store the output queue.

## Explanation
The problem can be solved greedily by sorting the people. We first sort them by height in descending order. If two people have the same height, we sort them by their k-value in ascending order. After sorting, we iterate through the list and insert each person into a new list at the index equal to their k-value. This works because all people already placed in the queue are taller than or equal in height to the current person. Thus, inserting the current person at index 'k' ensures that there are exactly 'k' taller/equal people in front of them, without violating the conditions of the people already placed.

## Solution
```python
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        # Sort people: 
        # 1. Descending order of height (h)
        # 2. Ascending order of k-value (k) for same heights
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        for p in people:
            # Since we process taller people first, the index where we insert the 
            # current person is exactly their k-value because all people already 
            # in the queue are taller than or equal in height to the current person.
            queue.insert(p[1], p)
            
        return queue
```
