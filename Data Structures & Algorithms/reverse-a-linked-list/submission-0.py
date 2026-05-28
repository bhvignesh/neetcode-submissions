# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head and head.next is not None:
            values.append(head.val)
            head = head.next
        if head:
            values.append(head.val)
        
            head = ListNode(val = values[-1], next = None)
            pointer = head
            values = values[:-1]
            for i in values[::-1]:
                pointer.next = ListNode(val = i, next = None)
                pointer = pointer.next
            return head
        else:
            return None

        