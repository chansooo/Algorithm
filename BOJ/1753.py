import sys
import heapq


V, E = map(int, sys.stdin.readline().split())
K = int(input())

graph = [[] for _ in range(V+1)]
dist = [float('inf')] * (V+1)
dist[K] = 0

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

pq = []
heapq.heappush(pq, (0, K))

while(pq):
    curDist, curNode = heapq.heappop(pq)
    if dist[curNode] < curDist:
        continue
    for destNode, destDist in graph[curNode]:
        d = curDist + destDist
        if dist[destNode] > d:
            dist[destNode] = d
            heapq.heappush(pq, (d, destNode))

for i in range(V+1):
    if i == 0:
        continue
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])
