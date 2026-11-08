# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            res = ListNode()
            pointer = res
            while list1 and list2:
                if list1.val < list2.val:
                    pointer.next = list1
                    pointer = pointer.next
                    list1 = list1.next
                else:
                    pointer.next = list2
                    pointer = pointer.next
                    list2 = list2.next
            
            while list1:
                pointer.next = list1 
                pointer = pointer.next
                list1 = list1.next
            
            while list2:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next
            
            return res.next
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                merged.append(merge(l1, l2))
            lists = merged
        return lists[0]
