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