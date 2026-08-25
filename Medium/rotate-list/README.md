# [Medium] Rotate List

## Complexity
Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once to find its length and at most once more to locate the split point.
Space Complexity: O(1) auxiliary space, as the rotation is done in place by modifying pointers.

## Explanation
To rotate the list to the right by k places, we first compute the length of the list, $n$, and locate its tail. If the list is empty, has only one node, or $k = 0$, we return the head immediately. Otherwise, we form a circular linked list by connecting the tail to the head. The effective rotation is $k \pmod n$. The new head will be at index $n - (k \pmod n)$ from the start. We find the node just before this (the new tail) by taking $n - (k \pmod n) - 1$ steps from the original head. Finally, we record the new head, break the circular connection by setting the new tail's next pointer to null, and return the new head.

## Solution
```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Compute the length of the list and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Connect the tail to the head to make it a circular list
        tail.next = head
        
        # Step 3: Find the new tail and new head
        # The new head is at position (length - k % length)
        # The new tail is at position (length - k % length - 1)
        k = k % length
        steps_to_new_tail = length - k - 1
        
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        # Step 4: Break the circle
        new_tail.next = None
        
        return new_head
```
