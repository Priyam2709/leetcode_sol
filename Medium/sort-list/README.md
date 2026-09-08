# [Medium] Sort List

## Complexity
Time Complexity: O(n log n), where n is the number of nodes in the list. The list is processed in log n phases, and each phase takes O(n) time to split and merge.
Space Complexity: O(1) auxiliary space, as the iterative bottom-up approach works in-place and does not use the call stack.

## Explanation
To sort the linked list in O(n log n) time complexity and O(1) auxiliary space, we implement a bottom-up (iterative) Merge Sort. 

1. First, we find the total length of the linked list.
2. We then progressively merge sublists of increasing lengths: 1, 2, 4, 8, etc., doubling the step size at each iteration.
3. The helper function `split` detaches a sublist of a given `size` from the rest of the list and returns the start of the remaining list.
4. The helper function `merge` merges two sorted linked lists in-place, returning both the head and the tail of the merged result.
5. We keep updating the links from a dummy starting node, avoiding recursive function calls and thus achieving true O(1) extra memory.

## Solution
```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Count the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        dummy = ListNode(0)
        dummy.next = head
        
        step = 1
        while step < length:
            curr = dummy.next
            tail = dummy
            while curr:
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step)
                
                merged_head, merged_tail = self.merge(left, right)
                tail.next = merged_head
                tail = merged_tail
            step *= 2
            
        return dummy.next
        
    def split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        curr = head
        for _ in range(size - 1):
            if not curr:
                break
            curr = curr.next
        if not curr:
            return None
        next_part = curr.next
        curr.next = None
        return next_part
        
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        while tail.next:
            tail = tail.next
        return dummy.next, tail
```
