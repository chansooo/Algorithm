from collections import defaultdict, deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    max = 102
    board = [[-1]* max for _ in range(max)]
    visited = [[0] * max for _ in range(max)]
    for rec in rectangle:
        min_x, min_y, max_x, max_y = map(lambda x: x * 2, rec)
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                # 내부
                if min_x < i < max_x and min_y < j < max_y:
                    board[i][j] = 0
                elif board[i][j] != 0:
                    board[i][j] = 1
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited[characterX*2][characterY*2] = 1
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        x, y = q.popleft()
        if x == itemX*2 and y == 2*itemY:
            return (visited[x][y] - 1) // 2
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if visited[nx][ny] == 0 and board[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
            
    return -1
















# def solution(rectangle, characterX, characterY, itemX, itemY):
#     count = 0
#     line_dict = defaultdict(set)
#     visited = [[False]* 51 for _ in range(51) ]
#     # 모든 좌표 넣기
#     for rec in rectangle:
#         # y에 대해서 가능한 x들을 전부 넣고, 최소 최대만 남긴다.
#         min_x, min_y, max_x, max_y = rec
#         print(rec)
#         a1 = [nx for nx in range(min_x, max_x + 1)]
#         a2 = [nx for nx in range(min_x, max_x + 1)]
#         line_dict[min_y] = line_dict[min_y] | (set(a1) | set(a2))
#         line_dict[max_y] = line_dict[max_y] | (set(a1) | set(a2))
#         for i in range(min_y, max_y + 1):
#             line_dict[i] = line_dict[i] | { min_x, max_x }
#     print("dict: ", line_dict)
#     # 갈 수 없는 좌표 빼기
#     for y in line_dict:
#         min_val = min(line_dict[y])
#         max_val = max(line_dict[y])
#         line_dict[y] = { min_val, max_val }
#     print("dict: ", line_dict)
#     #bfs
#     q = deque()
#     q.append([(characterX, characterY)])
#     while q:
#         cur_points = q.popleft()
#         count += 1
#         # 탈출 조건

#         if (itemX,itemY) in cur_points:
#             return count
#         # if visited[cur_x][cur_y]:
#             # continue
#         # visited[cur_x][cur_y] = True
#         # 상하좌우로 갈 수 있는 좌표 q에 삽입
        
#         temp_list = []
#         for cur_x, cur_y in cur_points:
#             next_x_list = line_dict[cur_y]
#             print("curx, y", cur_x, cur_y)
#             print("next_list", next_x_list)
#             if cur_x + 1 in next_x_list and not visited[cur_x+1][cur_y]:
#                 temp_list.append((cur_x + 1, cur_y))
#                 visited[cur_x+1][cur_y] = True
#             if cur_x - 1 in next_x_list and not visited[cur_x-1][cur_y]:
#                 temp_list.append((cur_x - 1, cur_y))
#                 visited[cur_x-1][cur_y] = True
#             if cur_x in line_dict[cur_y + 1] and not visited[cur_x][cur_y+1]:
#                 temp_list.append((cur_x, cur_y + 1))
#                 visited[cur_x][cur_y+1] = True
#             if cur_x in line_dict[cur_y - 1] and not visited[cur_x][cur_y-1]:
#                 temp_list.append((cur_x, cur_y - 1))
#                 visited[cur_x][cur_y-1] = True
#         if not temp_list:
#             q.append(temp_list)    
#     return -1