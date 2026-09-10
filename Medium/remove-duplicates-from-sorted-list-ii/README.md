# [Medium] Remove Duplicates from Sorted List II

## Complexity
Time Complexity: O(N) where N is the number of nodes in the linked list, as we traverse each node at most twice. Space Complexity: O(1) because we perform the operations in-place with a few pointers.

## Explanation
The problem requires us to remove all occurrences of duplicate numbers from a sorted linked list. To handle edge cases like removing the head node, we use a dummy node pointing to the head. We use a predecessor pointer `pred` to keep track of the last node before any sequence of duplicates. As we iterate through the list with the `head` pointer, if we detect duplicates (`head.val == head.next.val`), we advance the `head` pointer to the last node of the duplicate sequence and link `pred.next` to `head.next`, effectively removing all duplicates. If no duplicate is detected, we simply advance the `pred` pointer. Finally, we return `dummy.next`.

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        dummy = ListNode(0, head)
        # 'pred' tracks the node immediately before the sublist of duplicates
        pred = dummy
        
        while head:
            # If it's a start of a duplicate sublist
            if head.next and head.val == head.next.val:
                # Move till the end of the duplicate sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates by linking pred to the node after duplicates
                pred.next = head.next
            else:
                # Otherwise, move pred to the next node
                pred = pred.next
            
            # Move head to the next node
            head = head.next
            
        return dummy.next
```
