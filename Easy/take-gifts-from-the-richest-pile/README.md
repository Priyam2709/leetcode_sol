# [Easy] Take Gifts From the Richest Pile

## Complexity
Time Complexity: $O(n + k \log n)$, where $n$ is the number of gift piles and $k$ is the number of seconds. Heapifying takes $O(n)$ time, and each of the $k$ iterations performs heap operations taking $O(\log n)$ time.

Space Complexity: $O(n)$ to store the heap containing negated values of the gifts.

## Explanation
To repeatedly find and reduce the pile with the maximum number of gifts efficiently, we use a max-heap (simulated in Python by storing negated values in a standard min-heap). 

1. First, we convert the `gifts` array into a max-heap in $O(n)$ time.
2. In each of the $k$ seconds, we extract the maximum pile using `heappop`, calculate its integer square root using `math.isqrt`, and push the reduced count back into the heap using `heappush`.
3. After performing this operation $k$ times, we calculate and return the sum of all elements remaining in the heap.

## Solution
```python
import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Negate all elements to simulate a max-heap using Python's min-heap (heapq)
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            # Extract the maximum number of gifts
            largest = -heapq.heappop(max_heap)
            # Reduce to the floor of square root
            reduced = math.isqrt(largest)
            # Push the reduced value back into the heap
            heapq.heappush(max_heap, -reduced)
            
        # Return the sum of remaining gifts
        return -sum(max_heap)
```
