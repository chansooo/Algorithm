from heapq import heapify, heappush, heappop
# 쉬운 것부터
# 제약 사항 따라서
N, M = map(int, input().split())
result = []
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
pq = []
heapify(pq)
# 순서 그래프 만들기
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

#바로진입할 수 있는 애들 선별
for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(pq, i)
#print(pq)
while pq:
    #가장 작은 값 뱉음
    a = heappop(pq)
    result.append(a)
    for i in graph[a]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(pq, i)

print(' '.join(str(a) for a in result))
