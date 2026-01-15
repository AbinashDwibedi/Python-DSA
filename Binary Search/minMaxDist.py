import heapq
class MaxPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, dist, idx):
        heapq.heappush(self.heap, (-dist, idx))

    def pop(self):
        dist, idx = heapq.heappop(self.heap)
        return -dist, idx

    def top(self):
        dist, idx = self.heap[0]
        return -dist, idx

class Solution:
    def minMaxDist(self, stations, k):
        pq = MaxPriorityQueue()
        n = len(stations)
        if n <= 1:
            return 0.0
        for i in range(n - 1):
            pq.push(stations[i+1] - stations[i], i)

        howMany = [0] * (n - 1)

        for _ in range(k):
            dist, idx = pq.pop()
            howMany[idx] += 1

            original = stations[idx+1] - stations[idx]
            newDist = original / (howMany[idx] + 1)

            pq.push(newDist, idx)

        return pq.top()[0]

