# [Hard] Merge k Sorted Lists

## Complexity
Time Complexity: O(N log k), where N is the total number of nodes across all linked lists, and k is the number of linked lists. Each heap insertion and extraction takes O(log k) time, and we perform these operations for all N nodes.

Space Complexity: O(k) for the min-heap, as it stores at most one node from each of the k lists at any given time.

## Explanation
This solution uses a Min-Heap (Priority Queue) to efficiently merge $k$ sorted linked lists. 

1. We initialize a min-heap and push the head node of each non-empty linked list into it. To prevent comparison errors between `ListNode` objects when their values are identical, we push a tuple `(node.val, i, node)` where `i` is the index of the list. This serves as a unique tie-breaker.
2. We create a dummy node to easily construct and return the head of the merged linked list.
3. In a loop, we pop the smallest node from the heap, append it to our merged list, and advance the current pointer.
4. If the popped node has a next node, we push that next node into the heap.
5. We repeat this process until the heap is empty, and then return `dummy.next`.

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
        heap = []
        # Push the head of each list into the min-heap
        # We use the list index 'i' as a tie-breaker to prevent comparing ListNode objects directly
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
```
