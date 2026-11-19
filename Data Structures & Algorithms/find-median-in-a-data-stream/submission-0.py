class MedianFinder:

    def __init__(self):
        self.small = [] # max heap because we want the largest value from this 
        self.large = [] # min heap because we want the smallest value from this 
        
    def addNum(self, num: int) -> None:
        # add the number to the small heap first
        heapq.heappush(self.small, -num)
        
        # make sure every element in small is less than or equal to every element in large
        if (self.small and self.large and -self.small[0]>self.large[0]):
            # if our biggest value in small is bigger than our biggest value in large heap then we move the largest value to the bigger heap
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # now check if our small heap is a length of two smaller than our large heap, if it is we pop the smallest from large heap and move it to our small heap 
        if (len(self.small) + 2 == len(self.large)):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        if (len(self.large) + 2 == len(self.small)):
            heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0])/ 2.0
        
        