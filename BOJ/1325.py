import sys
import collections

def bfs(start):
  cnt = 1

  queue = collections.deque()
  queue.append(start)

  visited = [0 for _ in range(n+1)] 
  visited[start] = 1
  
  while queue:
    u = queue.popleft()
    for i in list[u]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1
        cnt +=1
        
  return cnt


n, m = map(int, sys.stdin.readline().split())
#딕셔너리
list = [[] for i in range(n+1)]

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  list[b].append(a)

result = []
max_cnt = 0

for i in range(1, n+1):
  cnt = bfs(i)
  if max_cnt == cnt:
    result.append(i)
  if cnt > max_cnt:
    max_cnt = cnt
    result = []
    result.append(i)


print(*result)