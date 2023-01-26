# 벽 3개를 세울 좌표를 뽑기
# 해당 벽을 세우고 난 후에 bfs 통해서 감염 진행
# 그 후 map에서 남아있는 0의 개수 세기

from itertools import combinations
from collections import deque
import copy

# bfs
def bfs(infest_grid, temp_map):
    d = [(1,0), (-1,0), (0,1), (0,-1)]
    # 전염시키기
    q = deque(copy.deepcopy(infest_grid))

    while q:
        cur_row, cur_col = q.popleft()
        for d_row, d_col in d:
            n_row = cur_row + d_row
            n_col = cur_col + d_col
            # if 0 <= n_row <= 
            if 0 <= n_row < row_num and 0 <= n_col < col_num and temp_map[n_row][n_col] == 0:
                temp_map[n_row][n_col] = 2
                q.append((n_row, n_col))
            
    # print()
    # print(temp_map)
    # print()
    # 0 개수 세기
    ret = 0
    for col in range(col_num):
        for row in range(row_num):
            if temp_map[row][col] == 0:
                ret += 1
    return ret 

row_num, col_num = map(int, input().split())
ans = 0
map_ = [ list(map(int, input().split())) for _ in range(row_num) ]

# 벽 3개 세울 좌표
# 0 ~ row_num, col_num까지의 숫자를 뽑고 같은 것이 있는 것들은 삭제.
empty_grid = []
infest_grid = []

for col_idx in range(col_num):
    for row_idx in range(row_num):
        if map_[row_idx][col_idx] == 0:
            empty_grid.append((row_idx, col_idx))
        elif map_[row_idx][col_idx] == 2:
            infest_grid.append((row_idx, col_idx))

possible_walls = list(combinations(empty_grid, 3))

# 가능한 벽 세울 수 있는 경우의 수 돌리기
for walls in possible_walls:
    # 벽 세우기
    temp_map = copy.deepcopy(map_)
    for row, col in walls:
        temp_map[row][col] = 1
    
    # 감염시키기
    cur_ans = bfs(infest_grid, temp_map)
    
    ans = max(ans, cur_ans)
        
print(ans)
