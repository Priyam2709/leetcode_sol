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