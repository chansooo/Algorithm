

house_num, route_num = map(int, input().split())    

parent = [i for i in range(house_num + 1)]

def find_parent(x):
    if x == parent[x]:
        return x
    else:
        y = find_parent(parent[x])
        parent[x] = y
        return y

def union_parent(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a > parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

l = []
for _ in range(route_num):
    l.append(list(map(int, input().split())))

l.sort(key = lambda x: x[2])

selected = []

result = 0

for node in l:
    a, b, cost = node
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        selected.append(cost)
        result += cost

result -= selected.pop()

print(result)