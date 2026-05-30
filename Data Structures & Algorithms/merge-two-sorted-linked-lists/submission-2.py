class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None

        while list1 and list2:
            if list1.val < list2.val:
                if not head:
                    head = list1
                    curr = head
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    curr = head
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next

        # attach remaining (list1 or list2)
        if not head:
            head = list1 or list2
        else:
            curr.next = list1 or list2

        return head