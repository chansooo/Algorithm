from turtle import position


N, M = map(int,input().split())
x, y, direction = map(int,input().split())
map = []

for i in range(N):
    map[i] = list(map(int, input().split()))

d = [[0]*M for _ in range(N)]


print(x, y, direction)

# 0:북, 1:동, 2:남, 3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction =3

count =1
turn_time =0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if map[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        turn_time =0
        continue
    else: 
        turn_time+= 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time =0
        
print(count)