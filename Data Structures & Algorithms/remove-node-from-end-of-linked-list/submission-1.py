# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pointer = head
        dp = dummy
        k = 0
        while k < n:
            pointer = pointer.next 
            k += 1
        
        while pointer:
            dp = dp.next
            pointer = pointer.next
        
        dp.next = dp.next.next
        return dummy.next