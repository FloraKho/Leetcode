class MedianFinder:

    def __init__(self):
        #two heaps, large, small, minheap, maxheap
        #heaps should eb equal size
        
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) #implement a max heap
        # make sure every num small is <= every num in large
        if(self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            #some small heap is greater than large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        #uneven size?
        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            #odd length
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()