from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

# Custom print function to print the value of each element occuring after the iputted node
def print_list(node):
    if not node:
        return ValueError("Node does not exist")
    
    output_list = []
    while node:
        output_list.append(node.val)
        node = node.next

    return print(output_list)


class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        # If neither exist, return None.
        if not head1 and not head2:
            return None
        
        # If there is only 1 list, return it.
        if not head1:
            return head2
        if not head2:
            return head1
        
        # Check which is the smaller head, this will be the head of the new merged list.
        # a will be list1 pointer and b will be list2 pointer. These pointers will always be \n
        # the next available element in their respective lists.

        if head1.val < head2.val:
            new_head = head1
            a = head1.next
            b = head2
        else:
            new_head = head2
            a = head1
            b = head2.next
        
        # current_node will always be the most recently added element to our new merged list
        current_node = new_head

        # While there are still nodes in both lists
        while a and b:
            
            # Check which is smaller (a or b) and add it to the merged list
            if a.val < b.val:
                current_node.next = a
                current_node = a
                a = current_node.next
            else:
                current_node.next = b
                current_node = b
                b = current_node.next
        
        # if there are still nodes in either, link the rest of that list to the end of the merged list
        if a:
            current_node.next = a
        if b:
            current_node.next = b
        
        return new_head




sol = Solution()

# List1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)
print_list(head1) # [1,2,4]

# List2
c = ListNode(4)
b = ListNode(3,c)
head2 = ListNode(1,b)
print_list(head2) # [1,3,4]

print_list(sol.mergeTwoLists(head1, head2)) # [1, 1, 2, 3, 4, 4]
