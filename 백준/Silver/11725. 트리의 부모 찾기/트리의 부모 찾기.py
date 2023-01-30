import sys
from collections import deque

n = int(input())

graph = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque()
q.append(1)

ret = [0] * (n+1)

while q:
    cur = q.popleft()
    for avail in graph[cur]:
        if ret[avail] == 0:
            ret[avail] = cur
            q.append(avail)
            
for i in range(2, n+1):
    print(ret[i])