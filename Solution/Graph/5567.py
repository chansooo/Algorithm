from collections import deque
import sys


def bfs(start):
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in range(1, friend_count + 1):
            if visited[i] == 0 and graph[a][i] == 1:
                q.append(i)
                visited[i] = visited[a] + 1

friend_count = int(input())
list_count = int(input())
graph = [[0] * (friend_count + 1) for i in range(friend_count + 1)]
visited = [0 for i in range(friend_count + 1)]

for i in range(list_count):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
bfs(1)

cnt = 0
for i in range(2, friend_count + 1):
    if visited[i] < 4 and visited[i] != 0:
        cnt += 1

print(cnt)