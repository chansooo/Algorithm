from collections import deque

def floodFill(planet, x, y, visited):
    n = len(planet)
    m = len(planet[0])
    
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    region_count = 0
    while q:
        x, y = q.popleft()
        if planet[x][y] == 0:
            region_count = 1
            for i in range(4):
                nx, ny = (x + dx[i])%n, (y + dy[i])%m
                if nx < 0 or nx >= len(planet) or ny < 0 or ny >= len(planet[0]) or visited[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True
    return region_count

n, m = map(int, input().split())
planet = []
for i in range(n):
    row = list(map(int, input().split()))
    planet.append(row)

visited = [[False if planet[i][j] == 0 else True for j in range(m)] for i in range(n)]

region_count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            region_count += floodFill(planet, i, j, visited)

print(region_count)
