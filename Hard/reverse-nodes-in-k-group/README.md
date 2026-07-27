# [Hard] Reverse Nodes in k-Group

## Complexity
Time Complexity: O(N), where N is the number of nodes in the linked list. Each node is processed at most twice (once to find the k-th node and once to reverse). Space Complexity: O(1) auxiliary memory since the reversal is done iteratively using only a few pointers.

## Explanation
The solution employs an iterative approach to achieve O(1) auxiliary space. We use a dummy node to easily handle changes to the head of the list. We maintain a pointer 'group_prev' that always points to the node preceding the current group of size k. In each iteration, we look ahead to locate the k-th node. If fewer than k nodes remain, we stop. Otherwise, we reverse the k-group in-place. By initializing our reversal pointer 'prev' to the start of the next group, we seamlessly link the tail of the reversed group to the remaining nodes in a single pass. Finally, we connect the preceding group to the new head of the reversed group and advance 'group_prev' to the end of the reversed group.

## Solution
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Find the k-th node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            # kth is now the last node of the current k-group
            next_group_start = kth.next
            
            # Reverse the current k-group
            prev = next_group_start
            curr = group_prev.next
            first_node = curr  # This will become the end of the reversed group
            
            while curr != next_group_start:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Connect the previous part to the newly reversed head
            group_prev.next = kth
            
            # Move group_prev to the end of the newly reversed group
            group_prev = first_node
```
