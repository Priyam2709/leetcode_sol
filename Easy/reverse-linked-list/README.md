# [Easy] Reverse Linked List

## Complexity
Time Complexity: O(N), where N is the number of nodes in the linked list, as we traverse the list exactly once.
Space Complexity: O(1), as we only use a constant amount of extra space for the pointers.

## Explanation
This solution uses an iterative approach to reverse the singly linked list in-place. We maintain two pointers: `prev` (initialized to `None`) and `curr` (initialized to `head`). As we traverse the list, we temporarily store the next node, redirect the `next` pointer of `curr` to point to `prev`, and then shift both `prev` and `curr` one step forward. This reverses the list linkages one by one. Once `curr` becomes `None`, `prev` will be pointing to the new head of the reversed list.

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
```
