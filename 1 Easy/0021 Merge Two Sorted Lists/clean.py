from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        if not head1 and not head2:
            return None
        
        if not head1:
            return head2
        if not head2:
            return head1

        if head1.val < head2.val:
            new_head = head1
            a = head1.next
            b = head2
        else:
            new_head = head2
            a = head1
            b = head2.next
        
        current_node = new_head

        while a and b:
            if a.val < b.val:
                current_node.next = a
                current_node = a
                a = current_node.next
            else:
                current_node.next = b
                current_node = b
                b = current_node.next
        

        if a:
            current_node.next = a
        if b:
            current_node.next = b
        
        return new_head




