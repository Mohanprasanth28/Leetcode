# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_list = ListNode()
        current = add_list
        carry = 0

        while l1 or l2 or carry:
            new1 = l1.val if l1 else 0
            new2 = l2.val if l2 else 0

            total = new1 + new2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return add_list.next

