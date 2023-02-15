import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edge = []
    parent = [i for i in range(m+1)]
    ans = 0

    for i in range(n):
        x, y, z = map(int, input().split())
        edge.append((x, y, z)) #z: 가중치

    edge.sort(key=lambda x:x[2])

    for i in edge:
        x, y, z = i
        if find(x) != find(y):
            union(x, y)
        else:
            ans += z
    print(ans)