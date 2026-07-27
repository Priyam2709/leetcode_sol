# [Medium] Swap Nodes in Pairs

## Complexity
Time Complexity: O(N), where N is the number of nodes in the linked list. We traverse the list once. 
Space Complexity: O(1) auxiliary space, as the swap is performed in-place using only a few pointers.

## Explanation
The solution uses an iterative approach with a dummy node to easily manage swapping of head nodes. We maintain a 'prev' pointer that points to the node just before the pair we want to swap. In each iteration, we identify the 'first' and 'second' nodes of the pair. We adjust their pointers to reverse their order: 'first.next' points to the rest of the list, 'second.next' points back to 'first', and 'prev.next' points to 'second'. Finally, we advance 'prev' to 'first' (which is now the second element of the swapped pair) and repeat until fewer than two nodes remain.

## Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
            
            # Move the prev pointer to the end of the swapped pair
            prev = first
            
        return dummy.next
```
