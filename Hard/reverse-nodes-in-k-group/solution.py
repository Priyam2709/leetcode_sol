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