from collections import deque
# 연결되어있는 노드들 visited = true로 바꾸고 1 반환.
def bfs(target, computers, visited):
    # 이미 방문한 노드는 무시
    if visited[target]:
        return 0
    q = deque()
    # 출발지점과 연결된 
    q.append(target)
    visited[target] = True
    while q:
        start_node = q.popleft()
        for i in range(len(computers[start_node])):
            if computers[start_node][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i] = True
    return 1

def solution(n, computers):
    answer = 0
    visited = [False] * len(computers)

    for i in range(len(computers)):
        answer += bfs(i, computers, visited)
        
    return answer