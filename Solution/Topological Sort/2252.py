from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
queue = deque()
answer = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    temp = queue.popleft()
    answer.append(temp)
    for i in graph[temp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
        
print(*answer)