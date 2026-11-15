# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        dummy = ListNode(0)
        dp = dummy 

        cur = slow.next
        prev = None
        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        first = head

        while prev:
            t1, t2 = first.next, prev.next
            first.next = prev 
            prev.next = t1
            first = t1 
            prev = t2