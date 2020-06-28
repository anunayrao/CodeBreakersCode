class RecentCounter:
    
    '''
    Pseudocode:
    Datastructure: queue
    1. Append the time value in the queue as the granularity of ping is 1ms. So only one ping can be made at a certain time.
    2. Now for the total pings in 3000ms window remove the elements from the queue which are older than 3000 ms 
    3. Length of queue will give the total pings as at certain time only one ping can be made.
    '''

    def __init__(self):
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        total = 0
        while t-self.queue[0] > 3000:
            self.queue.popleft()
        
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)