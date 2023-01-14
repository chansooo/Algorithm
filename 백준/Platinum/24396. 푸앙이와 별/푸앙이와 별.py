import sys
from collections import deque

def bfs(n,r):
    que = deque()
    que.append(r)
    visited = set(range(1,n+1))
    visited.remove(r)
    path[r] = 0
    while que:
        cv = que.popleft()
        aj[cv] = set(aj[cv])
        for i in visited - aj[cv]:
            que.append(i)
            visited.remove(i)
            path[i] = path[cv]+1
                
n,m = map(int,input().split())
aj = [[j]for j in range(n+1)]
path = [-1 for _ in range(n+1)]
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    aj[u].append(v)
    aj[v].append(u)
bfs(n,1)

for i in range(1,n+1):
    print(path[i])