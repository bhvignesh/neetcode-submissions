# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while list1 and list2:
            if list1.val > list2.val:
                values.append(list2.val)
                list2 = list2.next
            else:
                values.append(list1.val)
                list1 = list1.next
        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next
        if values:
            head = ListNode(values[0], None)
            curr = head
            values = values[1:]
            for i in values:
                curr.next = ListNode(i, None)
                curr = curr.next
            return head
        else:
            None
