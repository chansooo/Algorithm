import sys
import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    dist = [INF] * (node_count + 1)
    dist[start] = 0
    while(pq):
        curDist, curNode = heapq.heappop(pq)
        if dist[curNode] < curDist:
            continue
        for destNode, destDist in graph[curNode]:
            d = curDist + destDist
            if dist[destNode] > d:
                dist[destNode] = d
                heapq.heappush(pq, (d, destNode))
    return dist

INF = sys.maxsize
node_count, line_count = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(node_count+1)]

for _ in range(line_count):
    start, dest, weight = map(int, sys.stdin.readline().split())
    graph[start].append((dest, weight))
    graph[dest].append((start, weight))
    
must1, must2 = map(int, sys.stdin.readline().split())

start_dist = dijkstra(1)
must1_dist = dijkstra(must1)
must2_dist = dijkstra(must2)

path1 = start_dist[must1] + must1_dist[must2] + must2_dist[node_count]
path2 = start_dist[must2] + must2_dist[must1] + must1_dist[node_count]

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)
