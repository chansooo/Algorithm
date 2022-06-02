n = int(input())

map = list(input() for _ in range(n))
seen = list(input() for _ in range(n))
answer = [['.'] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def findbomb():
    for i in range(n):
        for j in range(n):

            if map[i][j] == '.' and seen[i][j] == 'x':
                bomb = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n: # 리스트 좌표 벗어났을때
                        continue

                    if map[nx][ny] == '*':
                        bomb += 1
                answer[i][j] = bomb

            if map[i][j] == '*' and seen[i][j] == 'x':
                show_bomb()


def show_bomb():
    for i in range(n):
        for j in range(n):
            if map[i][j] == '*':
                answer[i][j] = '*'


findbomb()
for i in range(n):
    for j in range(n):
        print(answer[i][j], end='')
    print()
