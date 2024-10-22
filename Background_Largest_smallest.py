unordered_list = [5, 2, 8, 3, 1, 7, 4, 6]
import heapq
heap = list(unordered_list)
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heap)