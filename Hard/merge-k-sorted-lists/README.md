# [Hard] Merge k Sorted Lists

## Complexity
Time Complexity: O(N log k), where N is the total number of nodes across all lists, and k is the number of linked lists. Each of the N nodes is pushed into and popped from the heap of size at most k once, and each heap operation takes O(log k) time.
Space Complexity: O(k) auxiliary space, as the min-heap stores at most one node from each of the k lists at any given time.

## Explanation
The solution uses a Min-Heap (Priority Queue) to efficiently merge the k sorted linked lists. We first insert the head node of each non-empty list into the heap. The elements in the heap are stored as tuples of `(node.val, i, node)`, where `i` is the index of the list. This index serves as a tie-breaker in Python to avoid comparing the `ListNode` objects directly when two nodes have the same value. In each step, we pop the node with the smallest value from the heap, append it to the merged list, and if that node has a next element, we push its next element into the heap. This process continues until the heap is empty.

## Solution
```python
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        # Initialize the heap with the head of each non-empty linked list
        # We use 'i' as a unique identifier to prevent comparing ListNode objects directly
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
                
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
```
