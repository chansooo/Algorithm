import sys
from collections import deque

def bfs(n,r):
    q = deque()
    q.append(r)
    visited = set(range(1,n+1))
    visited.remove(r)
    answer[r] = 0
    while q:
        cur_node = q.popleft()
        cut[cur_node] = set(cut[cur_node])
        for i in visited - cut[cur_node]:
            q.append(i)
            visited.remove(i)
            answer[i] = answer[cur_node]+1
                
n,m = map(int,input().split())
cut = [[j]for j in range(n+1)]
answer = [-1 for _ in range(n+1)]
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    cut[u].append(v)
    cut[v].append(u)
bfs(n,1)

for i in range(1,n+1):
    print(answer[i])