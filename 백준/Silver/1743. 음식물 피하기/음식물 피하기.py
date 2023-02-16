import sys
from collections import deque
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# row, col 받아서 상하좌우에 쓰레기 있는지 확인
# 쓰레기 확인한 곳은 count 올려주기
# 확인한 곳은 값 2로 바꿔주기

def bfs(col, row):
    q = deque()
    q.append([col, row])
    graph[col][row] = -1
    ret = 1
    while q:
        c, r = q.popleft()
        
        for d_col, d_row in direction:
            n_col = c + d_col
            n_row = r + d_row
            if 0 < n_col <= col_len and 0 < n_row <= row_len and graph[n_col][n_row] == 1:
                q.append([n_col, n_row])
                graph[n_col][n_row] = 2
                ret += 1
    return ret

col_len, row_len, gar_num = map(int, input().split())

# 쓰레기 -> 1, 쓰레기 없음 -> 0
graph = [[0] * (row_len+1) for _ in range(col_len+1)]
# print("3개", col_len, row_len, gar_num)
for _ in range(gar_num):
    c, r = map(int, input().split())
    graph[c][r] = 1

ans = 1

for col in range(1, col_len+1):
    for row in range(1, row_len+1):
        if graph[col][row] == 1:
            ans = max(ans, bfs(col, row))

print(ans)