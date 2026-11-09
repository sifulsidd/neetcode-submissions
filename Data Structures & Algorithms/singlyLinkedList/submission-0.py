class ListNode:
    def __init__(self, val, next_node = None):
        self.value = val
        self.next = next_node 

class LinkedList:
    def __init__(self):
        # Use a dummy node 
        self.head = ListNode(0)
        self.tail = self.head 

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        insert_node = ListNode(val)
        # make the next node the values after the 0 from dummy node
        insert_node.next = self.head.next
        self.head.next = insert_node
        # check if the next node is null, basically means we inserted the first node, so we have to make it the tail
        if not insert_node.next:
            self.tail = insert_node

    def insertTail(self, val: int) -> None:
        insert = ListNode(val)
        self.tail.next = insert
        self.tail = insert


    def remove(self, index: int) -> bool:
        i = 0 
        # we start at head, because if this way we get to 1 link before the link we have to skip 
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            # check if next value is tail, and if it is we update it  
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
        
