# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur and cur.next:
            if cur.next.val in num:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        

        