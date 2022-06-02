
n = int(input())

map = []
mine = []

for i in range(n):
    map.append(list(input().split()))

for i in range(n):
    mine.append(list(input().split()))

print(map)

# for i in range(n):
#     for j in range(n):
#         if map[i][j] == '*':
#             mine[i][j] = 