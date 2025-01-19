# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length +=1
            cur = cur.next
        a = head
        for _ in range(k - 1):
            a = a.next
        b = head
        for _ in range(length - k):
            b = b.next
    
        a.val,b.val = b.val,a.val
        return head
        
        

        