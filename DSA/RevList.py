# Creating  A Revv Linked List 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def reverse_list(head):
        prev = None 
        current = head 
        while current:
            next_node = current.next
            current.next = prev 
            prev = current 
            current = next_node 
        return prev 

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)

reversed_head = ListNode.reverse_list(list1)

# Print the reversed list
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next
