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