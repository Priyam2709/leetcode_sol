# [Medium] Swap Nodes in Pairs

## Complexity
Time Complexity: O(N) where N is the number of nodes in the linked list, as we traverse the list in a single pass. Space Complexity: O(1) auxiliary space since the swaps are done in-place using a few pointers.

## Explanation
The problem is solved iteratively using a dummy node to easily handle the head of the list. We use three pointers: `prev` (initially pointing to the dummy node), `first` (the first node of the pair to be swapped), and `second` (the second node of the pair). In each iteration, we adjust the pointers so that `first` points to the node after `second`, `second` points to `first`, and `prev` points to `second`. Finally, we move the `prev` pointer to `first` and continue until we have fewer than two nodes left to swap.

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swapping nodes
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move the pointer forward for the next pair
            prev = first
            
        return dummy.next
```
