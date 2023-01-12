from collections import deque

def dfs(y, x, maps):
    col_len = len(maps)
    row_len = len(maps[0])
    q = deque()
    q.append((y, x, 1))
    while q:
        y, x, dist = q.popleft()
        if y >= col_len - 1 and x >= row_len - 1:
            return dist
        if maps[y][x] == 0:
            continue
        maps[y][x] = 0
        if x + 1 < row_len:
            q.append((y, x+1, dist+1))
        if x - 1 >= 0:
            q.append((y, x-1, dist+1))
        if y + 1 < col_len:
            q.append((y+1, x, dist + 1))
        if y - 1 >= 0:
            q.append((y-1, x, dist + 1))
    return -1
def solution(maps):
    return dfs(0, 0, maps)