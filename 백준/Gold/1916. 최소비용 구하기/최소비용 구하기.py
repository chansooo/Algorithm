from heapq import heapify, heappop, heappush
from collections import defaultdict, deque

city_num = int(input())
bus_num = int(input())
cost_table = defaultdict(list)
for _ in range(bus_num):
    s, e, cost = map(int, input().split())
    cost_table[s].append([e, cost])

start, end = map(int, input().split())

pq = []
dist = [float('inf')] * (city_num + 1)
heappush(pq, (start, 0))

while pq:
    cur_node, cur_dist = heappop(pq)
    if dist[cur_node] < cur_dist:
        continue
    for dest_node, dest_dist in cost_table[cur_node]:
        d = cur_dist + dest_dist
        if dist[dest_node] > d:
            dist[dest_node] = d
            heappush(pq,(dest_node, d))

print(dist[end])