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