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