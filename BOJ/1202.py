import sys
import heapq

N, K = map(int, input().split())
result = 0

jems = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = []
for _ in range(K):
  bags.append(int(sys.stdin.readline()))


jems.sort()
bags.sort()

heap = []

for bag in bags:
    while jems and bag >= jems[0][0]: 
        heapq.heappush(heap, -heapq.heappop(jems)[1]) 
    if heap:
        result += heapq.heappop(heap)
    elif not jems:
        break

result = -result
print(result)