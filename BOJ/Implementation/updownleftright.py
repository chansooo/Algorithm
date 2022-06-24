N = int(input())
command = input().split()
x, y = 1, 1

# 상하좌우 순서로 0,1,2,3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이걸로 for문 돌려서 if문 계속 안 쓸 수 있도록
move_types = ['U', 'D', 'L', 'R']

for i in range(N):
    if command[i] == 'R':
        x += dx[3]
        y += dy[3]
    elif command[i] == 'L':
        x += dx[2]
        y += dy[2]
    elif command[i] == 'U':
        x += dx[0]
        y += dy[0]
    elif command[i] == 'D':
        x += dx[1]
        y += dy[1]
    else:
        x, y = -1, -1
        break

print(x, y)