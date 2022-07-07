# 인접한 칸을 방문해야하는 BFS문제라고 생각하고 큐를 이용해서 문제를 품
# 시간초과가 뜨는데 어떤 부분에서 시간을 잡아먹어서 시간초과가 뜨는지 잘 모르겠음
from collections import deque
def solution(n, m, image):
    answer = 0
    visited = [[False]*m for _ in range(n)]
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for x in range(n):
        for y in range(m):
            #방문하지 않은 칸이면 확인
            if not visited[x][y]:
                #현재 보고있는 칸의 숫자를 저장
                temp_num = image[x][y]
                queue = deque()
                queue.append((x, y))
                #같은 값의 인접한 칸들이 방문하지 않았다면 삽입하고 빌 때까지 돌리기
                while queue:
                    temp_x, temp_y = queue.popleft()
                    visited[temp_x][temp_y] = True
                    for i in range(4):
                        nx = temp_x + dx[i]
                        ny = temp_y + dy[i]
                        #맵 내에 있는지 확인
                        if nx >= 0 and nx < n and ny >= 0 and ny < m:
                            # 방문 안한 노드이고, 같은 숫자라면 큐에 삽입
                            if image[nx][ny] == temp_num  and visited[nx][ny] == False:
                                queue.append((nx, ny))
                # 큐가 끝났다면 이어질 수 있는 모든 칸이 방문된 것이므로 answer++  
                answer += 1
                
    return answer

n = 3
m = 2
image = [[1,2],[1, 2], [4,5]]
print(solution(n, m, image))