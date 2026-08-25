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