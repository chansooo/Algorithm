import sys
from heapq import heappush, heappop
inf = float('inf')
p1, p2 = map(int, input().split())

dp = [inf] * (100001)

pq = []

if p1 >= p2:
    print(p1 - p2)
    exit()
    
heappush(pq, (0, p1))

while pq:
    val, node = heappop(pq)
    for nx in [node + 1, node - 1, node * 2]:
        if 0 > nx or nx > 100000:
            continue
        if nx == node * 2 and dp[nx] == inf:
            dp[nx] = val
            heappush(pq, (val, nx))
        elif dp[nx] == inf:
            dp[nx] = val + 1
            heappush(pq, (val+1, nx))

print(dp[p2])