# 크루스칼 알고리즘
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
M = int(input())
# 각 node에서 처음 부모는 자신 node들 입니다
parent = [i for i in range(N+1)]

# 가장 상위 노드 찾기
def find_parent(x):
    if x == parent[x]:
        return x
    else:
        y = find_parent(parent[x])
        parent[x] = y
        return y

# 상위 노드 두개를 클 걸로 연결
def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a > parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


l = []
for _ in range(M):
    l.append(list(map(int, input().split())))
l.sort(key= lambda x : x[2])

result = 0

for node in l:
    a, b, cost = node
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)